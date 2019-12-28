from django.db import models
from user.models import HandyUser as User
from django.urls import reverse

# Create your models here.

class Message(models.Model):
	# TODO: Define fields here

	body = models.TextField()
	sender = models.ForeignKey(User,on_delete=models.CASCADE)
	recepient = models.ManyToManyField(User,related_name='receiver')
	sent_on = models.DateTimeField(auto_now_add=True)
	seen = models.BooleanField(default=False)
	sent = models.BooleanField(default=True)
	delivered = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Message"
		verbose_name_plural = "Messages"

	def __str__(self):
		recepients = ""
		for r in self.recepient.all():
			recepients = recepients + ", " + r.username
		recepients = recepients.strip(", ")
		return "From %s to %s" % (self.sender,recepients)


	# def get_absolute_url(self):
	# 	pass
		# return reverse("message:message", kwargs={"person":person})

	# TODO: Define custom methods here

		