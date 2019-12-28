from django.db import models
from user.models import HandyUser as User

# Create your models here.
class Client(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	phone = models.CharField(max_length=14,null=True)
	state = models.CharField(max_length=20,null=True) 
	city = models.CharField(max_length=20,null=True)
	home = models.CharField(max_length=150,null=True)
	work_email = models.EmailField(null=True)
	birth_date = models.DateField(null=True)
	image = models.ImageField(upload_to="clients")

	ONLINE_STATUS = (
  	("OF","Offline"),
  	("BU","Busy"),
  	("ON","Online"))
	online_status = models.CharField(max_length=2,choices=ONLINE_STATUS)
	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Clients"
	
	@property
	def address(self):
		home = self.home
		city = self.city
		state = self.state
		if self.home == None or len(self.home)<2:
		  home = ""
		if self.city == None or len(self.city)<2:
		  city = ""
		if self.state == None or len(self.state)<2:
		  state = ""
		address = home +", "+ city +", "+ state
		if len(address) <5:
		  return ""
		return address
  
	def __str__(self):
		return self.user.get_full_name()

	def get_absolute_url(self):
		return ('')
