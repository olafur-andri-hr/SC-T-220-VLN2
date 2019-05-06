from django.shortcuts import render, get_object_or_404
from .forms import PostalCodeForm
from django.http import JsonResponse
from django_countries import countries
from .models import PostalCode
# Create your views here.


def index(request):
    context = {
        "form": PostalCodeForm()
    }
    return render(request, 'location/index.html', context)


def get_town(request, country_code, postal_code):
    postal_code = get_object_or_404(
        PostalCode, zip_code=postal_code, country=country_code)
    country = postal_code.country
    response_data = {
        'country': {
            'name': country.name,
            'flag': country.flag,
            'flag_css': country.flag_css,
            'unicode_flag': country.unicode_flag,
            'code': country.code,
            'alpha3': country.alpha3,
            'numeric': country.numeric,
            'numeric_padded': country.numeric_padded,
        },
        'postal_code': postal_code.zip_code,
        'town': postal_code.town,
    }
    return JsonResponse(response_data)
