from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *


class CompanyInline(admin.StackedInline):
    model = Company
    can_delete = False
    verbose_name = 'Компания'

class UserAdmin(BaseUserAdmin):
    inlines = (CompanyInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)