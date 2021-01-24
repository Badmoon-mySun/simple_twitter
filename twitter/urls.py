from django.urls import path

from twitter.views import *

urlpatterns = [
    path('login/', login_view)
]