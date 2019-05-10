from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import redirect_to_login, LoginView
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from castleapartments.forms import SearchForm
from castleapartments.forms import LoginForm
from .forms import UserInfoForm, PostalCodeForm
from .models import PostalCode, Listing, ApartmentType
from apartments.utils import get_listing_results, get_page_info
from .utils import get_form_defaults


def index(request):
    if request.method == "POST":
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            listings, meta = get_listing_results(search_form)
        else:
            listings = Listing.objects.all()
            meta = get_page_info(search_form, listings)
            listings = listings[meta["offset"]:meta["end"]]
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
        "search_meta": meta
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
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/sell.html', context)


@login_required
def account(request):
    context = {
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/account.html', context)


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


def logout(request):
    django_logout(request)
    return redirect(index)
