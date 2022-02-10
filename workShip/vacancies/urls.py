from .views import *
from django.urls import path

urlpatterns = [
    path('', vacancies_home.as_view(), name='vacancies_home'),
    path('detail/<int:vacancy_id>/', vacancies_detail, name='vacancies_detail'),
    path('responses/<int:vacancy_id>/', vacancies_responses, name='vacancies_responses'),
    path('response/<int:response_id>/', vacancies_response_detail, name='vacancies_response_detail'),
    path('add/', vacancies_add, name='vacancies_add'),
    path('edit/<int:vacancy_id>/', vacancies_edit, name='vacancies_edit'),
    path('delete/<int:vacancy_id>/', vacancies_delete, name='vacancies_delete'),
]
