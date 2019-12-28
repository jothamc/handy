from django.urls import path, include
from .views import *

app_name = "contract"
urlpatterns = [
	path('',ContractList.as_view(),name="all"),
	path('<slug>-<pk>/',ContractView.as_view(),name="detail"),
]