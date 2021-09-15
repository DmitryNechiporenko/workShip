from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('indevelop/', views.in_develop, name='in_develop'),
    path('login/', LoginUser.as_view(), name='login'),
    path('passwordreset/', LoginUser.as_view(), name='password_reset'),
    path('logout/', logout_user, name='logout')
]
