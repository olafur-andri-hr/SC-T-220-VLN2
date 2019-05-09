from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:listing_id>', views.listing),
]
