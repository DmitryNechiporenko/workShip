from .views import *
from django.urls import path

urlpatterns = [
    path('', personal_account_home, name='personal_account_home'),
    path('edit/', personal_account_edit, name='personal_account_edit')
]
