from django.urls import path
from . import views

urlpatterns = [
    path('', views.time_entry_list, name='time_entry_list'),
    path('add/', views.add_time_entry, name='add_time_entry'),
]
