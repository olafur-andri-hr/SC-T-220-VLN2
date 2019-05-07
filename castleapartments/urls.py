from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('sell/', views.sell, name='sell'),
    path('account/', views.account, name='account'),
    path('listing/', views.listing, name='listing'),
]
