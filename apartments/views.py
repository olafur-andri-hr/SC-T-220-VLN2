from math import ceil
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.renderers import JSONRenderer
from .models import Listing, Apartment, ApartmentImage, ApartmentType
from castleapartments.models import PostalCode, Offer
from castleapartments.forms import SearchForm
from .serializers import ListingSerializer
from .utils import get_listing_results
from castleapartments.utils import get_form_defaults
from castleapartments.forms import OfferForm
from castleapartments.forms import CreditCardForm
# Create your views here.


def listing(request, listing_id):
    listing = Listing.objects.get(uuid=listing_id)
    all_offers = Offer.objects.filter(listing__uuid=listing_id)
    offer = None
    try:
        offer = Offer.objects.get(
            buyer__id=request.user.id,
            listing__uuid=listing_id
        )
    except Exception:
        pass
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "listing": listing,
        "offer": offer,
        "all_offers": all_offers
    }
    return render(request, 'castleapartments/apartmentinfo.html', context)


def search(request):
    if request.method == "GET":
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            results, meta = get_listing_results(search_form)
        else:
            search_form = SearchForm(get_form_defaults(SearchForm))
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


def offer(request, listing_id, offer_id):
    return HttpResponse("Showing offer: '{}' for listing: '{}'"
                        .format(offer_id, listing_id))


def newOffer(request, listing_id):
    listing = Listing.objects.get(uuid=listing_id)
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "offerform": OfferForm(),
        "creditcardform": CreditCardForm(),
        "listing": listing
    }
    return render(request, 'castleapartments/offer.html', context)
