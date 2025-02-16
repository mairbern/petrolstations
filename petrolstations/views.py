from django.shortcuts import render

# Create your views here.

from .models import PetrolStation

def petrol_station_list(request):
    stations = PetrolStation.objects.all()
    return render(request, 'petrolstations/petrol_station_list.html', {'stations': stations})