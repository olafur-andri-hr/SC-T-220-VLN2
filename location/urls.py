from django.urls import path

from . import views

urlpatterns = [
    path('<country_code>/<postal_code>', views.get_town, name='get town'),
    path('', views.index, name='index'),
]
