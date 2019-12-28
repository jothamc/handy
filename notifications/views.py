# from django.shortcuts import render
from .models import Notification
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


@method_decorator(login_required(),name="dispatch")
class NotificationsView(ListView):
	model = Notification
	template_name = "user/notif/index.html"
	context_object_name = "notifications"
	def get_queryset(self):
		user = self.request.user
		notifications = Notification.objects.filter(user=user).order_by("-datetime")
		# unseen = notifications.filter(seen=False)
		# self.extra_context = {"unseen":unseen}
	# 	self.get_unseen()
	# 	old_notifications = notifications.filter(seen_on__lt=timezone.now())
	# 	for n in old_notifications:
	# 		n.seen = True
	# 		n.save()
		return notifications
	# def get_unseen(self):
	# 	unseen = Notification.objects.filter(user=self.request.user,seen=False)
	# 	self.extra_context = {"unseen":unseen}
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	notifications = Notification.objects.filter(user=self.request.user)
	# 	# context['unseen'] = notifications.filter(seen=False)
	# 	return context

def JsonCount(request):
	user = request.user
	if user.is_authenticated:
		count = Notification.objects.filter(user=user,seen=False).count()
		data = {"count":count}
		return JsonResponse(data)
	else:
		return JsonResponse({"error":0})
	
