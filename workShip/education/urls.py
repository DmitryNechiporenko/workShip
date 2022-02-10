from . import views
from django.urls import path

urlpatterns = [
    path('', views.education_home, name='education_home'),
    path('detail/', views.study_detail, name='study_detail')
    #path('detail/', views.practice_detail, name='practice_detail'),
]
