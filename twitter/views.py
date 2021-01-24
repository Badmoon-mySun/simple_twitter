from django.shortcuts import render


def login_view(request):
    return render(request, 'twitter/login.html')


def registration_view(request):
    return render(request, '')

# Create your views here.
