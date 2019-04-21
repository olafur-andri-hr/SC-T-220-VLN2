from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models


def index(request):
    new_color = models.Color(color="red")
    new_color.save()
    new_car = models.Car(license_plate="ABC12", wheel_count=4,
                         color=new_color, manufacturer="Honda")
    new_car.save()
    vehicles = models.Vehicle.objects.all()
    context = {"cars": vehicles}
    return render(request, "index.html", context)
