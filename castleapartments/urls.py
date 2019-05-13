from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('sell/', views.sell, name='sell'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('account/editprofile/', views.editprofile, name='editprofile'),
    # path('listing/', views.listing, name='listing'),
    # path('listing/', views.listing, name='listing'),
    path('logout/', views.logout, name='logout'),
    path('listing/offer/', views.offer, name='offer')
]
