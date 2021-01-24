from django.urls import path

from twitter.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('tweet/<str:slug>/', tweet_view, name='tweet'),
    path('profile/', profile_view, name='profile'),
]