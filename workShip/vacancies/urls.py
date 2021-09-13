from . import views
from django.urls import path

urlpatterns = [
    path('', views.vacancies_home, name='vacancies_home'),
    path('detail/<int:vacancy_id>/', views.vacancies_detail, name='vacancies_detail'),
]
