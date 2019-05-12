from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
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
from .models import Offer
from apartments.utils import get_listing_results, get_page_info
from .utils import get_form_defaults
from django.forms.models import model_to_dict


def index(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        listings, meta = get_listing_results(search_form)
    else:
        defaults = get_form_defaults(SearchForm)
        search_form = SearchForm(defaults)
        search_form.full_clean()
        listings = Listing.objects.all().order_by(
            search_form.cleaned_data['order_by']
        )
        meta = get_page_info(search_form, listings)
        listings = listings[meta["offset"]:meta["end"]]
    apartment_types = ApartmentType.objects.all()
    len_listings = 0
    user_full_name = ""
    try:
        user_full_name = request.user.userinfo.first_name + " " + \
            request.user.userinfo.last_name
    except AttributeError:
        user_full_name = ""
    for listing in listings:
        if listing.processed:
            len_listings += 1
    context = {
        "listings": listings,
        "len_listings": len_listings,
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
    context = {
        "isAdmin": request.user.is_superuser,
        "authenticated": request.user.is_authenticated,
        "user": request.user,
        "form": SellForm()
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
        "saleRequests": sale_requests,
        "buyRequests": buy_reqests
    }
    return render(request, 'castleapartments/account.html', context)


def profile(request):
    listings = Listing.objects.filter(
        seller=request.user).reverse().exclude(sold_date__isnull=False)
    sold_listings = Listing.objects.exclude(sold_date__isnull=True)
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/profile.html', context)


def listing(request):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/listing.html', context)


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
            return redirect(account)
    else:
        user_info_form = UserInfoForm(instance=request.user.userinfo)
        user_form = UserCreationForm()
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
