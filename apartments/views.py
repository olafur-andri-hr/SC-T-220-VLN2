from math import ceil
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.renderers import JSONRenderer
from .models import Listing, Apartment, ApartmentImage, ApartmentType
from castleapartments.models import PostalCode, Offer
from django.contrib.auth.decorators import login_required
from castleapartments.forms import SearchForm
from .serializers import ListingSerializer
from .utils import get_listing_results
from castleapartments.utils import get_form_defaults, EmailUtil
from castleapartments.forms import OfferForm
from castleapartments.forms import CreditCardForm
# Create your views here.


def listing(request, listing_id):
    listing = get_object_or_404(Listing, uuid=listing_id)
    plus_address = listing.apartment.address.replace(' ', '+')
    all_offers = Offer.objects.filter(listing__uuid=listing_id)
    offer = None
    try:
        offer = Offer.objects.get(
            buyer__id=request.user.id,
            listing__uuid=listing_id
        )
    except Offer.DoesNotExist:
        pass
    accepted_offer = None
    try:
        accepted_offer = \
            Offer.objects.get(listing__uuid=listing.uuid, accepted=True)
    except Exception:
        pass
    if (not listing.processed) \
        and (request.user.id != listing.seller.id) \
            and (not request.user.is_superuser):
        return HttpResponseBadRequest()
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "listing": listing,
        "address_without_spaces": plus_address,
        "offer": offer,
        "all_offers": all_offers,
        "accepted_offer": accepted_offer
    }
    return render(request, 'castleapartments/apartmentinfo.html', context)


def list_listing(request, listing_id):
    a_listing = get_object_or_404(Listing, uuid=listing_id)
    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    elif not request.user.is_superuser:
        return HttpResponseBadRequest()
    a_listing.processed = True
    a_listing.save()

    # Return a response
    context = {
        "listing": a_listing
    }
    return redirect(listing, listing_id=a_listing.uuid)


def unlist_listing(request, listing_id):
    a_listing = get_object_or_404(Listing, uuid=listing_id)
    if not request.user.is_authenticated:
        return HttpResponseBadRequest()
    elif not request.user.is_superuser:
        return HttpResponseBadRequest()
    a_listing.processed = False
    a_listing.save()

    # Return a response
    context = {
        "listing": a_listing
    }
    return redirect(listing, listing_id=a_listing.uuid)


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
            listing = Listing.objects.get(
                uuid=listing_id,
                processed=True,
                sold_date=None,
            )
            data.append(
                ListingSerializer(
                    listing,
                    context={'request': request}
                ).data
            )
        except Exception:
            continue
    return JsonResponse(data, safe=False)


@login_required
def offer(request, listing_id, offer_id):
    user = request.user
    listing = get_object_or_404(Listing, uuid=listing_id)
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
    elif not listing.processed:
        return HttpResponseBadRequest()
    return render(request, 'castleapartments/viewoffer.html', context)


@login_required
def newOffer(request, listing_id):
    listing = get_object_or_404(Listing, uuid=listing_id)
    accepted_offer = None
    try:
        accepted_offer = \
            Offer.objects.get(listing__uuid=listing.uuid, accepted=True)
    except Exception:
        pass

    if accepted_offer:
        return HttpResponseBadRequest()
    elif not listing.processed:
        return HttpResponseBadRequest()

    try:
        old_offer = Offer.objects.get(buyer=request.user, listing=listing)
    except Offer.DoesNotExist:
        old_offer = None
    new_offer = None
    if request.method == "POST":
        offer_form = OfferForm(request.POST)
        credit_card_form = CreditCardForm(request.POST)
        if offer_form.is_valid() and credit_card_form.is_valid() and \
                request.user != listing.seller:
            if old_offer:
                old_offer.credit_card.delete()
                old_offer.delete()
            cc = credit_card_form.save()
            new_offer = Offer(
                buyer=request.user,
                listing=listing,
                request_amount=offer_form.cleaned_data["offer_amount"],
                request_date=offer_form.cleaned_data["conveyance_date"],
                credit_card=cc,
            )
            new_offer.save()
            EmailUtil.send_offer_email(new_offer)
    else:
        offer_form = OfferForm()
        credit_card_form = CreditCardForm()
        if old_offer:
            offer_form = OfferForm(
                data={
                    "offer_amount": old_offer.request_amount,
                    "conveyance_date": old_offer.request_date
                }
            )
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "offerform": offer_form,
        "creditcardform": credit_card_form,
        "listing": listing,
        "offer": new_offer
    }
    return render(request, 'castleapartments/offer.html', context)


@login_required
def accept_offer(request, listing_id, offer_id):
    listing = get_object_or_404(Listing, uuid=listing_id)
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
    elif not listing.processed:
        return HttpResponseBadRequest()
    offer.accepted = True
    offer.save()

    # Return a response
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "listing": listing
    }
    return render(request, 'castleapartments/acceptoffer.html', context)


@login_required
def decline_offer(request, listing_id, offer_id):
    listing = get_object_or_404(Listing, uuid=listing_id)
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
    elif not listing.processed:
        return HttpResponseBadRequest()

    # Decline the offer
    Offer.objects.get(id=offer_id).delete()

    # Return a response
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "listing": listing
    }
    return render(request, 'castleapartments/declineoffer.html', context)


@login_required
def delete_listing(request, listing_id):
    success = True
    listing = None
    try:
        listing = get_object_or_404(Listing, uuid=listing_id)
        if (not request.user == listing.seller
                and not request.user.is_superuser):
            return HttpResponseBadRequest()
        listing.delete()
        send_mail(
            "Your listing '{}' has been deleted"
            .format(listing.apartment.address),
            "We must inform you that your listing '{}' has "
            .format(listing.apartment.address) +
            "been from the Castle Apartments website. For more info, " +
            "feel free to contact us. Phone: +354 123 4567, email: " +
            "castleapartments.vln2@gmail.com",
            "castleapartments.vln2@gmail.com",
            [listing.seller.userinfo.email],
            fail_silently=True
        )
    except Listing.DoesNotExist:
        success = False
    context = {
        "listing": listing,
        "success": success,
        "authenticated": request.user.is_authenticated,
        "user": request.user
    }
    return render(request, 'castleapartments/deletelisting.html', context)


def cancel_offer_prompt(request, listing_id, offer_id):
    listing = get_object_or_404(Listing, uuid=listing_id)
    offer = Offer.objects.get(id=offer_id)
    if request.user.id != offer.buyer.id:
        return HttpResponseBadRequest()
    context = {
        "user": request.user,
        "authenticated": request.user.is_authenticated,
        "listing": listing,
        "offer": offer
    }
    return render(request, 'castleapartments/canceloffer.html', context)


def cancel_offer(request, listing_id, offer_id):
    offer = get_object_or_404(Offer, id=offer_id)
    if request.user.id != offer.buyer.id:
        return redirect(listing, listing_id=listing_id)
    offer.delete()
    return redirect(listing, listing_id=listing_id)
