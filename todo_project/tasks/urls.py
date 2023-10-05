from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for the home view
    path('list/', views.task_list, name='task_list'),  # List tasks view
    path('create/', views.create_task, name='create_task'),  # Create task view
]
