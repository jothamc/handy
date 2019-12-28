from django.contrib import admin
from .models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    '''
        Admin View for Notification
    '''
    list_display = ('message','user','notification_type')
    list_filter = ('notification_type',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('message',)

admin.site.register(Notification, NotificationAdmin)