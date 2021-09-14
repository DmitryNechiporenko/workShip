from django.contrib import admin
from .models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'company', 'landing')
    list_editable = ('is_published',)
    list_filter = ('company', 'landing', 'time_create', 'is_published')


admin.site.register(Vacancy, VacancyAdmin)