from . import views
from django.urls import path

urlpatterns = [
    path('', views.seaman_home, name='seaman_home'),
]
