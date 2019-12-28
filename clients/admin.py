from django.contrib import admin
from .models import Client
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
	'''
	Admin View for 
	'''
	list_display = ('user',)
	# list_filter = ('full_name',)
	search_fields = ('user',)

admin.site.register(Client, ClientAdmin)