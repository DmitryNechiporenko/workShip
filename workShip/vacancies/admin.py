from django.contrib import admin
from .models import Vacancy


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'user', 'landing')
    list_editable = ('is_published',)
    list_filter = ('user', 'landing', 'time_create', 'is_published')


admin.site.register(Vacancy, VacancyAdmin)