from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Профиль'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)