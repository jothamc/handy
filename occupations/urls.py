from django.urls import path
from .views import IndexView, OccupationDetail

app_name = "occupations"
urlpatterns = [
	path("",IndexView.as_view(),name="index"),
	path("<slug>/",OccupationDetail.as_view(),name="detail"),
]