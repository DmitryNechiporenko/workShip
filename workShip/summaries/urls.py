from . import views
from django.urls import path

urlpatterns = [
    path('', views.summaries_home, name='summaries_home'),
    path('detail/', views.summaries_detail, name='summaries_detail'),
]
