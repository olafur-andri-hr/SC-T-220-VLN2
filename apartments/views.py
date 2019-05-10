from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.renderers import JSONRenderer
from .models import Listing, Apartment, ApartmentImage, ApartmentType
from castleapartments.models import PostalCode
from castleapartments.forms import SearchForm
from .serializers import ListingSerializer
# Create your views here.


def listing(request, listing_id):
    listing = Listing.objects.get(uuid=listing_id)
    return HttpResponse(f"This is the listing for {listing.apartment.address}")


def search(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            parameters = search_form.cleaned_data
            types = parameters["type"].values("id")
            query = {
                "apartment__address__icontains": parameters["address"],
                "apartment__postal_code__zip_code": parameters["zip_code"],
                "apartment__postal_code__country": parameters["country"],
                "apartment__postal_code__town": parameters["town"],
                "apartment__num_rooms__gte": parameters["min_rooms"],
                "apartment__num_rooms__lte": parameters["max_rooms"],
                "apartment__appraisal__gte": parameters["min_price"] * 1000000,
                "apartment__appraisal__lte": parameters["max_price"] * 1000000,
                "apartment__size__gte": parameters["min_size"],
                "apartment__size__lte": parameters["max_size"],
                "apartment__apartment_type__id__in": types,
                "processed": True
            }
            for key, value in list(query.items()):
                if value is None or value == '':
                    del query[key]
            results = Listing.objects.filter(**query)
            # apartments = [res.apartment for res in results]
            # a = apartments[0]
            # apartment_types = [apt.apartment_type for apt in apartments]
            # apartment_images = list()
            # for apt in apartments:
            #     for image in apt.apartmentimage_set.all():
            #         apartment_images.append(image)
            # stuff = [
            #     *results, *apartments, *apartment_types, *apartment_images
            # ]
            # json_results = serializers.serialize(
            #     'json', stuff, ensure_ascii=False
            # )
            serializer = ListingSerializer(
                results, many=True,  context={'request': request}
            )
            json = JSONRenderer().render(serializer.data).decode('UTF-8')
            return JsonResponse(json, safe=False)
    return HttpResponseBadRequest()
