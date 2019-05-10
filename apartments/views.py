from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Listing
from castleapartments.forms import SearchForm

# Create your views here.


def listing(request, listing_id):
    listing = Listing.objects.get(uuid=listing_id)
    return HttpResponse(f"This is the listing for {listing.apartment.address}")


def search(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            parameters = search_form.cleaned_data
            results = Listing.objects.filter(parameters)
            return JsonResponse(results)


def get_many_by_id(request, listing_ids):
    id_list = listing_ids.split(",")
    data = []
    for listing_id in id_list:
        listing = Listing.objects.get(uuid=listing_id)
        data.append({
            "image": listing.apartment.apartmentimage_set.first().image.url,
            "listing_date": listing.listing_date,
            "address": listing.apartment.address,
            "zip_code": listing.apartment.postal_code.zip_code,
            "town": listing.apartment.postal_code.town,
            "country": listing.apartment.postal_code.country.name,
            "apt_number": listing.apartment.apt_number,
            "type": listing.apartment.apartment_type.name,
            "num_rooms": listing.apartment.num_rooms,
            "price": listing.apartment.appraisal,
            "description": listing.apartment.description,
            "uuid": listing_id,
        })
    return JsonResponse(data, safe=False)
