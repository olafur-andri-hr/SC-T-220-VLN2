from django.contrib import admin

# Register your models here.
from .models import Color, Vehicle, Car, Scooter
from .models import User, Town

admin.site.register(Color)
admin.site.register(Vehicle)
admin.site.register(Car)
admin.site.register(Scooter)
admin.site.register(User)
admin.site.register(Town)
