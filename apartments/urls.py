from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:listing_id>/', views.listing, name="listing"),
    path('<uuid:listing_id>/offer/', views.newOffer, name='newOffer'),
    path('<uuid:listing_id>/offers/<int:offer_id>/', views.offer),
    path(
        '<uuid:listing_id>/offers/<int:offer_id>/accept/',
        views.accept_offer
    ),
    path(
        '<uuid:listing_id>/offers/<int:offer_id>/decline/',
        views.decline_offer
    ),
    path(
        '<uuid:listing_id>/list/',
        views.list_listing
    ),
    path(
        '<uuid:listing_id>/unlist/',
        views.unlist_listing
    ),
    path('api/search/', views.search),
    path('api/search/<str:listing_ids>/', views.get_many_by_id)
]
