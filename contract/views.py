from django.views.generic import ListView,DetailView,UpdateView
from .models import Contract,Application

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

login_url = "/user/login/"

class ContractView(DetailView):
	model = Contract
	template_name = "contract.html"
	context_object_name = "contract"
	query_pk_and_slug = True



@method_decorator(login_required(login_url=login_url),name="dispatch")
class ContractList(ListView):
	model = Contract
	template_name = "all_contracts.html"
	context_object_name = "contracts"
	ordering = ['-created_on']

class Application(UpdateView):
	pass
