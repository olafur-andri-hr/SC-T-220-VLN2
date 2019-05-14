from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('sell/', views.sell, name='sell'),
    path('profiles/<int:user_id>/', views.profile, name='profiles'),
    path('account/', views.account, name='account'),
    path('account/editprofile/', views.editprofile, name='editprofile'),
    path('buyrequest/<int:offer_id>/', views.asale, name="buyrequest"),
    # path('listing/', views.listing, name='listing'),
    # path('listing/', views.listing, name='listing'),
    path('logout/', views.logout, name='logout')
]
