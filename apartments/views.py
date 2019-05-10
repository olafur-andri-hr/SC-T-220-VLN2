from math import ceil
from django.shortcuts import render
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
            result_count = len(results)
            page_count = ceil(result_count / parameters["per_page"])
            page_number = parameters['page_number']
            parameters["per_page"]
            # results = results
            serializer = ListingSerializer(
                results, many=True,  context={'request': request}
            )
            response = {"listings": serializer.data, 'meta': {
                'result_count': result_count,
                'page_count': page_count,
                'page_number': parameters['page_number'],
            }}
            print(response)
            json = JSONRenderer().render(response).decode('UTF-8')
            return JsonResponse(json, safe=False)
    return HttpResponseBadRequest()


def get_many_by_id(request, listing_ids):
    id_list = listing_ids.split(",")
    data = []
    for listing_id in id_list:
        listing = Listing.objects.get(uuid=listing_id)
        # data.append({
        #     "image": listing.apartment.apartmentimage_set.first().image.url,
        #     "listing_date": listing.listing_date,
        #     "address": listing.apartment.address,
        #     "zip_code": listing.apartment.postal_code.zip_code,
        #     "town": listing.apartment.postal_code.town,
        #     "country": listing.apartment.postal_code.country.name,
        #     "apt_number": listing.apartment.apt_number,
        #     "type": listing.apartment.apartment_type.name,
        #     "num_rooms": listing.apartment.num_rooms,
        #     "price": listing.apartment.appraisal,
        #     "description": listing.apartment.description,
        #     "uuid": listing_id,
        # })
    return JsonResponse(data, safe=False)
