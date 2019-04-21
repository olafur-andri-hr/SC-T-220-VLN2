from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models


def index(request):
    vehicles = models.Vehicle.objects.all()
    context = {"cars": vehicles}
    return render(request, "index.html", context)
