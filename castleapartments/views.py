from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import redirect_to_login, LoginView
from django.contrib.auth.models import User
from castleapartments.forms import SearchForm
from castleapartments.forms import LoginForm
from .forms import UserInfoForm, PostalCodeForm
from .models import PostalCode, Listing
from django.urls import reverse


def index(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings,
        "form": SearchForm(),
        "authenticated": request.user.is_authenticated,
        "user": request.user,
    }
    return render(request, 'castleapartments/index.html', context)


def about(request):
    return render(request, 'castleapartments/about.html')


def login(request):
    return LoginView.as_view(
        form_class=LoginForm,
        template_name='castleapartments/login.html',
        extra_context={"authenticated": False}
    )(request)


def sell(request):
    context = {"authenticated": request.user.is_authenticated,
               "user": request.user}
    if not request.user.is_authenticated:
        return redirect_to_login(reverse(sell))
    return render(request, 'castleapartments/sell.html', context)


def account(request):
    return render(request, 'castleapartments/account.html')


def listing(request):
    return render(request, 'castleapartments/listing.html')


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
            postal_code.save()

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
    }
    return render(request, 'castleapartments/signup.html', context)


def logout(request):
    django_logout(request)
    return redirect(index)
