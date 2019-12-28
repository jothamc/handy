from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from workers.models import Worker
from clients.models import Client
from occupations.models import Occupation

# Create your models here.
WORK_STATUS = (
	("NB","Not Begun"),
	("AC","Active"),
	("CO","Completed")
)
WORK_TYPE = (
	("ST","Short Term"),
	("LT","Long Term"),
	("OT","One Time")
)

class Contract(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	client = models.ForeignKey(Client,on_delete=models.CASCADE)
	workers = models.ManyToManyField(Worker)
	wage = models.IntegerField(default=0)
	slug = models.SlugField(null=True)
	work_type = models.CharField(max_length=2,choices=WORK_TYPE,default='OT')
	client_approved = models.BooleanField(default=False)
	worker_done = models.BooleanField(default=False)
	work_status = models.CharField(max_length=2,choices=WORK_STATUS,default='NB')
	rating = models.SmallIntegerField(default=0)
	created_on = models.DateTimeField(auto_now_add=True)
	edited_on = models.DateTimeField(auto_now=True)
	finished_on = models.DateTimeField(null=True,editable=False)
	occupations = models.ManyToManyField(Occupation)
	num_of_workers = models.SmallIntegerField(default=1)
	years_of_experience = models.SmallIntegerField(default=0)
	location = models.CharField(max_length=300,default="")

	class Meta:
		verbose_name = "Contract"
		verbose_name_plural = "Contracts"

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("contract:detail",kwargs={"pk":self.id,"slug":self.slug})

	def finished(self):
		if self.client_approved==True and self.worker_done==True:
			self.work_status = "CO"
			now = timezone.now()
			self.finished_on = now
			return True
		return False
	def save(self,*args,**kwargs):
		value = self.title
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args,**kwargs)
		
		    
class Application(models.Model):
	contract = models.ForeignKey(Contract,on_delete=models.CASCADE)
	worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
	applied_on = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	seen = models.BooleanField(default=False)
	accepted = models.BooleanField(default=False)

	class Meta:
		verbose_name='Application'
		verbose_name_plural = 'Applications'

	def __str__(self):
		return "%s's application to %s" % (self.worker.user.username,self.contract.title)

	def get_absolute_url(self):
		pk = self.contract.pk
		slug = self.contract.slug
		return reverse("jobs:applied",kwargs={"pk":pk,"slug":slug})