from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/day-<int:day_number>/', views.project_detail, name='project_detail'),
]
