from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from castleapartments.forms import SearchForm
from castleapartments.forms import LoginForm
from .forms import UserInfoForm, PostalCodeForm
from .models import PostalCode


def index(request):
    context = {
        "form": SearchForm()
    }
    return render(request, 'castleapartments/index.html', context)


def about(request):
    return render(request, 'castleapartments/about.html')


def login(request):
    context = {
        "form": LoginForm()
    }
    return render(request, 'castleapartments/login.html', context)


def sell(request):
    return render(request, 'castleapartments/sell.html')


def account(request):
    return render(request, 'castleapartments/account.html')


def listing(request):
    return render(request, 'castleapartments/listing.html')


def signup(request):
    if request.method == "POST":
        user_info_form = UserInfoForm(request.POST, request.FILES)
        postal_code_form = PostalCodeForm(request.POST)
        user_form = UserCreationForm(request.POST)
        # print(user_info_form.is_valid())

        if (user_form.is_valid() and postal_code_form.is_valid() and
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
            redirect(index)
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
