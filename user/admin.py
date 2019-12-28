from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from .models import HandyUser
# Register your models here.

class HandyUserAdmin(UserAdmin):
  fieldsets = (
      (None, {'fields': ('username', 'password')}),
      (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
      (_('Permissions'), {
          'fields': ('is_client','is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
      }),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('username', 'password1', 'password2'),
      }),
  )
  list_filter = ('is_client','is_staff', 'is_superuser', 'is_active', 'groups')
  ordering = ('-is_staff','username',)
  list_display = ('username','is_client')

admin.site.register(HandyUser, HandyUserAdmin)