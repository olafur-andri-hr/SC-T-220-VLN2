from django.shortcuts import render
from castleapartments.forms import SearchForm


def index(request):
    context = {
        "form": SearchForm()
    }
    return render(request, 'castleapartments/index.html', context)


def about(request):
    return render(request, 'castleapartments/about.html')


def login(request):
    return render(request, 'castleapartments/login.html')


def sell(request):
    return render(request, 'castleapartments/sell.html')


def signup(request):
    return render(request, 'castleapartments/signup.html')
