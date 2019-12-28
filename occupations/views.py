from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Occupation

# Create your views here.
class IndexView(ListView):
	model = Occupation
	template_name = "occupations/index.html"
	context_object_name	= "occupations"
	queryset = Occupation.objects.order_by("name")

class OccupationDetail(DetailView):
	model = Occupation
	template_name = "occupations/detail.html"