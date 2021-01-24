from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from twitter.forms import CustomUserCreationForm, CustomUserAuthForm
from twitter.models import Tweet


def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password do not right')
    else:
        form = CustomUserAuthForm()
    return render(request, 'twitter/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'twitter/registration.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def tweet_view(request, slug):
    tweet = Tweet.objects.get(slug=slug)

    if request.method == 'POST':
        text = request.POST.get('tweet_comment')
        new_tweet = Tweet(author=request.user, body=text, replying_tweet=tweet)
        new_tweet.save()

    comments = Tweet.objects.filter(replying_tweet=tweet)
    context = {'tweet': tweet, 'comments': comments, 'username': request.user.get_username()}

    return render(request, 'twitter/tweet.html', context)


@login_required
def profile_view(required):
    pass


def home_view(request):
    tweets = Tweet.objects.all()[:10]
    return render(request, 'twitter/home.html', {'tweets': tweets, 'username': request.user.get_username()})
