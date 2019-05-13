from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:listing_id>/', views.listing),
    path('<uuid:listing_id>/offers/<int:offer_id>', views.offer),
    path('api/search/', views.search),
    path('api/search/<str:listing_ids>/', views.get_many_by_id)
]
