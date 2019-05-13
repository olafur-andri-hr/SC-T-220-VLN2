from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import redirect_to_login, LoginView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
from castleapartments.forms import LoginForm
from .forms import SellForm
from .forms import UserInfoForm, PostalCodeForm
from .models import PostalCode, Listing, ApartmentType
from .models import Offer, Listing, Apartment, ApartmentImage
from apartments.utils import get_listing_results, get_page_info
from .utils import get_form_defaults
from django.forms.models import model_to_dict
from .forms import CreditCardForm
from .forms import OfferForm


def index(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        listings, meta = get_listing_results(search_form)
    else:
        defaults = get_form_defaults(SearchForm)
        search_form = SearchForm(defaults)
        search_form.full_clean()
        listings = Listing.objects.filter(
            processed=True, sold_date=None
        ).order_by(
            search_form.cleaned_data['order_by']
        )
        meta = get_page_info(search_form, listings)
        listings = listings[meta["offset"]:meta["end"]]
    apartment_types = ApartmentType.objects.all()
    user_full_name = ""
    try:
        user_full_name = request.user.userinfo.first_name + " " + \
            request.user.userinfo.last_name
    except AttributeError:
        user_full_name = ""
    context = {
        "listings": listings,
        "len_listings": meta["result_count"],
        "form": search_form,
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "user_full_name": user_full_name,
        "apartment_types": apartment_types,
        **meta,
        "pages": range(1, meta["page_count"] + 1),
    }
    return render(request, 'castleapartments/index.html', context)


def about(request):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/about.html', context)


def login(request):
    return LoginView.as_view(
        form_class=LoginForm,
        template_name='castleapartments/login.html',
        extra_context={
            "authenticated": request.user.is_authenticated,
            "user": request.user,
        }
    )(request)


@login_required
def sell(request):
    form = SellForm()
    postal_code_form = PostalCodeForm()
    listing = None
    if request.method == "POST":
        form = SellForm(request.POST, request.FILES)
        postal_code_form = PostalCodeForm(request.POST)
        if form.is_valid() and postal_code_form.is_valid():
            postal_code = postal_code_form.get_postal_code()
            data = form.cleaned_data
            apartment = Apartment(
                postal_code=postal_code,
                address=data["address"],
                apt_number=data["apt_number"],
                appraisal=data["appraisal"],
                num_rooms=data["num_of_rooms"],
                num_bathrooms=data["num_of_toilets"],
                size=data["size"],
                apartment_type=data["type"],
                description=data["description"],
                garage_parking_space=data["garage"],
                year_built=data["year_built"],
            )
            apartment.save()
            # print(apartment.save())
            files = request.FILES.getlist('images')
            apartment_images = list()
            for image in files:
                apt_image = ApartmentImage(
                    apartment=apartment,
                    image=image
                )
                apt_image.full_clean()
                apartment_images.append(apt_image)
            for img in apartment_images:
                img.save()
            listing = Listing(
                apartment=apartment,
                seller=request.user,
            )
            listing.save()
    context = {
        "isAdmin": request.user.is_superuser,
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "form": form,
        "postal_code_form": postal_code_form,
        "listing": listing
    }
    return render(request, 'castleapartments/sell.html', context)


@login_required
def account(request):
    listings = Listing.objects.filter(
        seller=request.user).reverse().exclude(sold_date__isnull=False)
    sold_listings = Listing.objects.exclude(sold_date__isnull=True)
    sale_requests = Listing.objects.filter(
        processed=False)
    buy_reqests = Offer.objects.filter(
        accepted=True).filter(processed=False)
    context = {
        "authenticated": request.user.is_authenticated,
        "isAdmin": request.user.is_superuser,
        "user": request.user,
        "listings": listings,
        "soldlistings": sold_listings,
    }
    if request.user.is_superuser:
        ifaddmin = {
            "saleRequests": sale_requests,
            "buyRequests": buy_reqests
        }
        context.update(ifaddmin)
    return render(request, 'castleapartments/account.html', context)


def profile(request, profile_id):
    user_profile = User.objects.get(uuid=profile_id)
    listings = Listing.objects.filter(
        seller=request.user).reverse().exclude(sold_date__isnull=False)
    sold_listings = Listing.objects.exclude(sold_date__isnull=True)
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/profile.html', context)


def offer(request):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "offerform": OfferForm(),
        "creditcardform": CreditCardForm()
    }
    return render(request, 'castleapartments/offer.html', context)


def signup(request):
    if request.method == "POST":
        user_info_form = UserInfoForm(request.POST, request.FILES)
        postal_code_form = PostalCodeForm(request.POST)
        user_form = UserCreationForm(request.POST)

        if user_info_form.is_valid():
            changed_data = dict(request.POST)
            changed_data['username'] = user_info_form.cleaned_data["email"]
            user_form = UserCreationForm(data=changed_data)

        if (postal_code_form.is_valid() and user_form.is_valid() and
                user_info_form.is_valid()):
            new_user = user_form.save()

            postal_code = postal_code_form.get_postal_code()

            new_user_info = user_info_form.save(commit=False)
            new_user_info.postal_code = postal_code
            new_user_info.user = new_user
            new_user_info.save()
            if new_user.is_active:
                request.session.set_expiry(86400)  # time to session expiry
                django_login(request, new_user)
            return redirect(index)
    else:
        user_form = UserCreationForm()
        user_info_form = UserInfoForm()
        postal_code_form = PostalCodeForm()

    context = {
        "user_form": user_form,
        "user_info_form": user_info_form,
        "postal_code_form": postal_code_form,
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/signup.html', context)


@login_required
def editprofile(request):
    if request.method == "POST":
        user_form = PasswordChangeForm(request.user, request.POST)
        user_info_form = UserInfoForm(
            request.POST, request.FILES, instance=request.user.userinfo)
        postal_code_form = PostalCodeForm(request.POST)

        if (postal_code_form.is_valid() and user_form.is_valid() and
                user_info_form.is_valid()):
            new_user = user_form.save()

            postal_code = postal_code_form.get_postal_code()

            new_user_info = user_info_form.save(commit=False)
            new_user_info.postal_code = postal_code
            new_user_info.save()
            if new_user.is_active:
                request.session.set_expiry(86400)  # time to session expiry
                django_login(request, new_user)

            return redirect(account)
    else:
        user_info_form = UserInfoForm(instance=request.user.userinfo)
        user_form = PasswordChangeForm(user=request.user)
        postal_code_form = PostalCodeForm(
            data=model_to_dict(request.user.userinfo.postal_code))

    context = {
        "user_form": user_form,
        "user_info_form": user_info_form,
        "postal_code_form": postal_code_form,
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/editprofile.html', context)


def logout(request):
    django_logout(request)
    return redirect(index)
