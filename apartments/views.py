from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
