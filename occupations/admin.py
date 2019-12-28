from django.contrib import admin
from .models import Occupation
# Register your models here.
class OccupationAdmin(admin.ModelAdmin):
    '''
        Admin View for Occupation
    '''
    # fields = ['name','slug']
    list_display = ('name',"slug")
    # list_filter = ('',)
    # inlines = [
    #     # Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('name',"slug","description")

admin.site.register(Occupation, OccupationAdmin)