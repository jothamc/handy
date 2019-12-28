from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Occupation(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	slug = models.SlugField(default='',editable=False)#max_length=settings.OCCUPATION_NAME_MAX_LENGTH
	class Meta:
		verbose_name = "Occupation"
		verbose_name_plural = "Occupations"
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		kwargs = {
			'pk':self.id,
			'slug':slug
		}
		return reverse("slug-pk",kwargs=kwargs)
	def save(self,*args,**kwargs):
		value = self.name
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args,**kwargs)