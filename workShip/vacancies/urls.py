from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', vacancies_home.as_view(), name='vacancies_home'),
    path('detail/<int:vacancy_id>/', vacancies_detail, name='vacancies_detail'),
    path('responses/<int:vacancy_id>/', vacancies_responses, name='vacancies_responses'),
    path('response/<int:response_id>/', vacancies_response_detail, name='vacancies_response_detail'),
    path('add/', vacancies_add, name='vacancies_add')
]
