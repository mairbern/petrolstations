from django.urls import path
from . import views

urlpatterns = [
    path('', views.petrol_station_list, name='petrol_station_list'),
]
 