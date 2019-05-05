from django.shortcuts import render
from .forms import PostalCodeForm
# Create your views here.


def index(request):
    context = {
        "form": PostalCodeForm()
    }
    return render(request, 'location/index.html', context)
