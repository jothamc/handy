from django.urls import path, include
from .views import *

app_name = "workers"
urlpatterns = [
	path("",WorkersList.as_view(),name="all"),
	path("<slug:username>/",WorkerDetail.as_view(),name="detail"),
]