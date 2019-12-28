from django.urls import path,include
from .views import *

app_name = "notifications"
urlpatterns=[
	path('',NotificationsView.as_view(),name="list"),
	path("json-count/",JsonCount,name="json_count"),
]