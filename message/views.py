from django.shortcuts import render
from django.views.generic import ListView,CreateView
from user.models import HandyUser as User
from .models import Message
from django.db.models import Q
from collections import Counter
# Create your views here.

class MessageInboxView(ListView):
	model = Message
	template_name = "message/messages.html"
	context_object_name = "messages"
	def get_queryset(self):
		messages = Message.objects.filter(recepient=self.request.user).order_by("-sent_on")
		persons = [p.sender.username for p in messages]
		count = Counter(persons)

		##Impement a for loop that checks if an entry is from a user already entered and delete it, leaving only the most recent
		self.extra_context = {"persons":persons,"count":count}
		return messages


def MessageView(request,person):
	sender = User.objects.get(username=person)
	messages = Message.objects.filter(
		Q(recepient=request.user,sender=sender) |
		Q(sender=request.user,recepient=sender)
	).order_by("sent_on")
	return render(request,"message/message.html",{"messages":messages})



class MessageSendView(CreateView):
	model = Message
	fields = ['body']
	template_name = "message/message.html"
	context_object_name = "messagef"
	def form_valid(self,form):
		form.instance.sender = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
	  recepient_user = self.kwargs.get('recepient')
	  recepients = User.objects.get(username=recepient_user)
	  self.object.recepient.add(recepients)
	  return "/messages/%s/" % recepient_user



	 ##fix sending to self observed in chrome using user jothamc
	 ## work on js polling or sockets
	 ## work on design
	 ## work on create message
	 ## work on 404