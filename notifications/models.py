from django.db import models
from user.models import HandyUser as User

# Create your models here.

class Notification(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	NOTIFICATION_TYPE = (
		("AA","Job Application Accepted"),
		("AD","Job Application Denied"),
		("NA","New Application"),
		("CN","Contract Notification")
	)
	notification_type = models.CharField(max_length=3,choices=NOTIFICATION_TYPE)
	message = models.TextField()
	datetime = models.DateTimeField(auto_now_add=True)
	seen = models.BooleanField(default=False)
	seen_on = models.DateTimeField(auto_now=True)
	# other_users = models.ManyToManyField(User)
	class Meta:
		verbose_name = "Notification"
		verbose_name_plural = "Notifications"
	def __str__(self):
		return self.message

	def create_message(self,*,notification_type=None,contract=None,application_count=None,message=None):
		notification_type = self.notification_type or notification_type
		if notification_type == "AA":
			contract = contract.title
			message = "Your Application to '%s' has been accepted" % contract

		elif notification_type == "AD":
			contract = contract.title
			message = "Your Application to '%s' has been denied" % contract

		elif notification_type == "NA":
			count = application_count + 1
			contract = contract.title
			message = "Contract '%s' has %d new Application(s)" % (contract,count)

		elif notification_type == "CN":
			message = "Contract '%s' notification: %s" % (contract,parameters)

		self.message = message
		return message

	def get_absolute_url(self):
		return "/user/notifications/"