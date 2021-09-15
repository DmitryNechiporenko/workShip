from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', vacancies_home.as_view(), name='vacancies_home'),
    path('detail/<int:vacancy_id>/', views.vacancies_detail, name='vacancies_detail'),
]
