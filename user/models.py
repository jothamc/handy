from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class HandyUser(AbstractUser):
	is_client = models.BooleanField("Is A Client",default=False)
	class Meta:
		verbose_name='HandyUser'
		verbose_name_plural='HandyUsers'