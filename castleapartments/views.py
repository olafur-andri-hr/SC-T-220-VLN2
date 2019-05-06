from django.shortcuts import render
from castleapartments.forms import SearchForm
from castleapartments.forms import LoginForm
from castleapartments.forms import SignUpForm


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


def signup(request):
    signup = SignUpForm()
    signup_left = [
        signup.cleaned_data[first_name],
        signup.last_name,
        signup.ssn,
        signup.dob,
        signup.email,
        signup.phone,
        signup.password
    ]
    signup_right = [
        signup.country,
        signup.zip_code,
        signup.town,
        signup.address,
        signup.aptN
    ]
    context = {
        "form": SignUpForm(),
        "form_left": signup_left,
        "form-right": signup_right
    }
    return render(request, 'castleapartments/signup.html', context)
