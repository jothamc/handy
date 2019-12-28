from django.contrib import admin
from .models import Contract,Application

# Register your models here.
class ContractAdmin(admin.ModelAdmin):
    '''
        Admin View for Contract
    '''
    list_display = ('title','client')
    list_filter = ('title','client')
    search_fields = ('title','client')

class ApplicationAdmin(admin.ModelAdmin):
    '''
        Admin View for Application
    '''
    list_display = ("__str__",'applied_on',)
    list_filter = ('applied_on','seen')
    search_fields = ('__str__','message')

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Contract, ContractAdmin)