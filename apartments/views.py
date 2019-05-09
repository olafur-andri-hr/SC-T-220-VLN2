from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing

# Create your views here.


def listing(request, listing_id):
    listing = Listing.objects.get(uuid=listing_id)
    return HttpResponse(f"This is the listing for {listing.apartment.address}")
