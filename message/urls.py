from django.urls import path, include
from .views import *

app_name = "message"
urlpatterns = [
	path("",MessageInboxView.as_view(),name="list"),
	path("<person>/",MessageView,name="message"),
	path("<recepient>/send/",MessageSendView.as_view(),name="send"),
]