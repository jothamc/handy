from django.shortcuts import render
from  django.views.generic import DetailView,ListView
from .models import Worker
from user.models import HandyUser as User
from occupations.models import Occupation
# Create your views here.

class WorkersList(ListView):
	model = Worker
	template_name = "workers/index.html"
	context_object_name = "workers"

class WorkerDetail(DetailView):
	context_object_name = "worker"
	template_name = "workers/profile.html"
	occupations = Occupation.objects.all()
	extra_context = {"occupations":occupations}
	def get_object(self):
		username = self.kwargs.get('username')
		worker = Worker.objects.get(user__username=username)
		return worker
