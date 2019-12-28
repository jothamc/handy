from django.contrib import admin
from .models import Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    '''
        Admin View for Message
    # '''
    list_display = ('__str__','sent_on')
    list_filter = ('sent_on',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('body','sender','recepient',)

admin.site.register(Message, MessageAdmin)