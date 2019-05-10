from math import ceil
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from .models import Listing, Apartment, ApartmentImage, ApartmentType
from castleapartments.models import PostalCode
from castleapartments.forms import SearchForm


def get_listing_results(search_form: SearchForm):
    search_form.is_valid()
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
    results = Listing.objects.filter(**query).order_by(
        parameters["order_by"])
    meta = get_page_info(search_form)
    return results[meta["offset"]:meta["end"]], meta


def get_page_info(search_form: SearchForm, results):
    search_form.full_clean()
    try:
        parameters = search_form.cleaned_data
    except AttributeError:
        parameters = search_form.initial
    per_page = parameters.get("per_page", 24)
    page_number = parameters.get("page_number", 1)
    offset = (page_number - 1) * per_page
    end = offset + per_page
    result_count = len(results)
    page_count = ceil(result_count / per_page)
    return {
        'result_count': result_count,
        'page_count': page_count,
        'page_number': parameters['page_number'],
        'offset': offset,
        'end': end
    }
