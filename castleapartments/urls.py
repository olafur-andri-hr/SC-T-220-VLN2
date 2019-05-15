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
    path('buyrequest/<int:offer_id>/complete/', views.complete_buyrequest),
    path('buyrequest/<int:offer_id>/decline/', views.decline_buyrequest),
    path('logout/', views.logout, name='logout')
]
