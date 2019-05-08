from django.contrib import admin
from .models import Apartment, ApartmentType, ApartmentImage, Listing

# Register your models here.
admin.site.register(Apartment)
admin.site.register(ApartmentImage)
admin.site.register(ApartmentType)
admin.site.register(Listing)
