from . import views
from django.urls import path

urlpatterns = [
    path('', views.services_home, name='services_home'),
]
