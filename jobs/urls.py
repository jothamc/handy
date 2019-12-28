from django.urls import path, include
from .views import *

app_name = "jobs"
urlpatterns = [
	path('',ContractList.as_view(),name="all"),
	path('page-<int:page>/',ContractPage.as_view(),name="page"),
	path('<slug>-<pk>/',ContractView.as_view(),name="detail"),
	path('<slug>-<pk>/apply/',ContractApplyView.as_view(),name="apply"),
	path('<slug>-<pk>/application/',ContractApplied.as_view(),name="applied"),
	path('search/',SearchView.as_view(),name="search"),
	path('search/<item>/',SearchView.as_view(),name="search_item"),
]