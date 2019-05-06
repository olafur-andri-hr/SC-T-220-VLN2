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
    context = {
        "form": SignUpForm()
    }
    return render(request, 'castleapartments/signup.html', context)
