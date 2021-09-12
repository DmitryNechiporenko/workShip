from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('indevelop/', views.in_develop, name='in_develop'),
]
