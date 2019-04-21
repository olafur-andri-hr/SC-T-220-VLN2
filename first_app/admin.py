from django.contrib import admin

# Register your models here.
from .models import Color, Vehicle, Car, Scooter

admin.site.register(Color)
admin.site.register(Vehicle)
admin.site.register(Car)
admin.site.register(Scooter)
