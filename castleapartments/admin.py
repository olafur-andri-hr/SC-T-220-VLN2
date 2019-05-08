from django.contrib import admin

from .models import UserInfo, Apartment, ApartmentImage, ApartmentType
from .models import Listing, Offer, CreditCard
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Apartment)
admin.site.register(ApartmentImage)
admin.site.register(ApartmentType)

admin.site.register(Listing)
admin.site.register(Offer)
admin.site.register(CreditCard)
