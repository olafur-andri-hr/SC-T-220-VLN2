from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.db.models.Model import DoesNotExist
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
        user_info_form = UserInfoForm(request.POST)
        postal_code_form = PostalCodeForm(request.POST)
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            user_info_form.initial['user'] = new_user

        if postal_code_form.is_valid():
            zip_code = postal_code_form.cleaned_data["postal_code"]
            country = postal_code_form.cleaned_data["country"]
            try:
                postal_code = PostalCode.objects.get(
                    postal_code=zip_code, country=country
                )
            except DoesNotExist:
                postal_code = postal_code_form.save(commit=False)
            user_info_form.initial['postal_code'] = new_postal_code

        if user_info_form.is_valid():
            new_user_info = user_info_form.save(commit=False)
            print("IT WORKERD!!!!")
        else:
            for item in user_info_form.errors:
                print(item)

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
