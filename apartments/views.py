from math import ceil
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.renderers import JSONRenderer
from .models import Listing, Apartment, ApartmentImage, ApartmentType
from castleapartments.models import PostalCode
from castleapartments.forms import SearchForm
from .serializers import ListingSerializer
from .utils import get_listing_results
# Create your views here.


def listing(request, listing_id):
    listing = Listing.objects.get(uuid=listing_id)
    context = {
        "listing": listing
    }
    return render(request, 'castleapartments/apartmentinfo.html', context)


def search(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            results, meta = get_listing_results(search_form)
            serializer = ListingSerializer(
                results, many=True,  context={'request': request}
            )
            response = {"listings": serializer.data, 'meta': meta}
            return JsonResponse(response, safe=False)
    return HttpResponseBadRequest()


def get_many_by_id(request, listing_ids):
    id_list = listing_ids.split(",")
    data = []
    for listing_id in id_list:
        listing = Listing.objects.get(uuid=listing_id)
        data.append(
            ListingSerializer(
                listing,
                context={'request': request}
            ).data
        )
    return JsonResponse(data, safe=False)
