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
    accepted_offer = None
    try:
        accepted_offer = \
            Offer.objects.get(listing__uuid=listing.uuid, accepted=True)
    except Exception:
        pass
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "listing": listing,
        "offer": offer,
        "all_offers": all_offers,
        "accepted_offer": accepted_offer
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
        try:
            listing = Listing.objects.get(uuid=listing_id)
            data.append(
                ListingSerializer(
                    listing,
                    context={'request': request}
                ).data
            )
        except Exception:
            pass
    return JsonResponse(data, safe=False)


def offer(request, listing_id, offer_id):
    user = request.user
    listing = Listing.objects.get(uuid=listing_id)
    offer = Offer.objects.get(id=offer_id)
    accepted_offer = None
    try:
        accepted_offer = \
            Offer.objects.get(listing__uuid=listing.uuid, accepted=True)
    except Exception:
        pass
    context = {
        "user": user,
        "authenticated": request.user.is_authenticated,
        "listing": listing,
        "offer": offer
    }

    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    elif request.user.id != listing.seller.id:
        return HttpResponseBadRequest()
    elif accepted_offer:
        return HttpResponseBadRequest()
    return render(request, 'castleapartments/viewoffer.html', context)


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


def accept_offer(request, listing_id, offer_id):
    listing = Listing.objects.get(uuid=listing_id)
    offer = Offer.objects.get(id=offer_id)
    accepted_offer = None
    try:
        accepted_offer = \
            Offer.objects.get(listing__uuid=listing.uuid, accepted=True)
    except Exception:
        pass

    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    elif request.user.id != listing.seller.id:
        return HttpResponseBadRequest()
    elif accepted_offer:
        return HttpResponseBadRequest()
    offer.accepted = True
    offer.save()

    # Return a response
    context = {
        "listing": listing
    }
    return render(request, 'castleapartments/acceptoffer.html', context)


def decline_offer(request, listing_id, offer_id):
    listing = Listing.objects.get(uuid=listing_id)
    accepted_offer = None
    try:
        accepted_offer = \
            Offer.objects.get(listing__uuid=listing.uuid, accepted=True)
    except Exception:
        pass

    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    elif request.user.id != listing.seller.id:
        return HttpResponseBadRequest()
    elif accepted_offer:
        return HttpResponseBadRequest()

    # Decline the offer
    Offer.objects.get(id=offer_id).delete()

    # Return a response
    context = {
        "listing": listing
    }
    return render(request, 'castleapartments/declineoffer.html', context)
