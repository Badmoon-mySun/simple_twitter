from django.urls import path

from twitter.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
]