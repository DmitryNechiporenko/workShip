from . import views
from django.urls import path

urlpatterns = [
    path('', views.company_home, name='company_home'),
]
