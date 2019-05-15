from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:listing_id>/', views.listing, name="Listing"),
    path('<uuid:listing_id>/offer/', views.newOffer, name='New offer'),
    path('<uuid:listing_id>/offers/<int:offer_id>/',
         views.offer, name="Offer"),
    path(
        '<uuid:listing_id>/delete/',
        views.delete_listing,
        name='Delete listing'
    ),
    path(
        '<uuid:listing_id>/offers/<int:offer_id>/accept/',
        views.accept_offer,
        name='Accept offer'
    ),
    path(
        '<uuid:listing_id>/offers/<int:offer_id>/decline/',
        views.decline_offer,
        name='Decline offer'
    ),
    path(
        '<uuid:listing_id>/list/',
        views.list_listing,
        name='New listing'
    ),
    path(
        '<uuid:listing_id>/unlist/',
        views.unlist_listing,
        name='Delete listing'
    ),
    path('api/search/', views.search, name='Search'),
    path('api/search/<str:listing_ids>/', views.get_many_by_id, name="Search by")
]
