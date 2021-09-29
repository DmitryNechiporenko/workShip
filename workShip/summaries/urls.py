from .views import *
from django.urls import path

urlpatterns = [
    path('', summaries_home.as_view(), name='summaries_home'),
    path('detail/<int:summary_id>/', summaries_detail, name='summaries_detail'),
    path('add/', summary_add, name='summary_add'),
    path('responses/<int:summary_id>/', summaries_responses, name='summaries_responses'),
    path('response/<int:response_id>/', summaries_response_detail, name='summaries_response_detail')

]
