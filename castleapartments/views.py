from django.shortcuts import render
from castleapartments.forms import SearchForm


def index(request):
    context = {
        "form": SearchForm()
    }
    return render(request, 'castleapartments/index.html', context)
