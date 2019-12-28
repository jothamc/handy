from django.views.generic import ListView,DetailView,CreateView,UpdateView
from contract.models import Contract,Application
from django.db.models import Q

# from occupations.models import Occupation
from clients.models import Client
from workers.models import Worker

from notifications.models import Notification

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class ContractView(DetailView):
	model = Contract
	template_name = "job_detail.html"
	context_object_name = "contract"
	query_pk_and_slug = True
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		applied = None
		if self.request.user.is_authenticated:
			if self.request.user.is_client is False:
				if Application.objects.filter(contract=self.get_object(),worker__user=self.request.user):
					applied = "Applied"
				context['applied'] = applied
			elif self.request.user.is_client:
				context['applied'] = "Clients cannot apply for jobs"
		return context


class ContractList(ListView):
	model = Contract
	template_name = "all_jobs.html"
	context_object_name = "contracts"
	ordering = ['-created_on']
	paginate_by = 2


class ContractPage(ListView):
	model = Contract
	template_name = "all_jobs.html"
	context_object_name = "contracts"
	ordering = ['-created_on']
	paginate_by = 2


@method_decorator(login_required(),name="dispatch")
class ContractApplyView(CreateView):
	model = Application
	template_name = "apply.html"
	context_object_name = "application"
	fields = ['message']

	def form_valid(self,form):
		slug = self.kwargs.get('slug')
		pk = self.kwargs.get('pk')
		form.instance.contract = Contract.objects.get(slug=slug,pk=pk)
		form.instance.worker = Worker.objects.get(user=self.request.user)
		applications = Application.objects.filter(contract = form.instance.contract,seen=False)
		notification = Notification(user=form.instance.contract.client.user,notification_type="NA")
		notification.create_message(
			contract = form.instance.contract,
			application_count = applications.count()
		)
		notification.save()
		return super().form_valid(form)

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    slug,pk = self.kwargs['slug','pk']
	    contract = Contract.objects.get(slug=slug,pk=pk)
	    context['contract']=contract
	    return context


@method_decorator(login_required(),name="dispatch")
class ContractApplied(DetailView):
	template_name = "application.html"
	context_object_name = "application"
	def get_object(self):
		pk,slug = self.kwargs['pk','slug']
		application = Application.objects.get(contract__slug=slug,contract__pk=pk,worker__user=self.request.user)
		return application



class SearchView(ListView):
	template_name = "search.html"
	context_object_name = "contracts"

	def get_queryset(self):
		item = self.kwargs.get('item') or ""
		self.extra_context = {"item": item}
		return Contract.objects.filter(
			Q(title__icontains=item) | 
			Q(description__icontains=item) |
			Q(occupations__name__icontains=item)
			).order_by("-created_on")