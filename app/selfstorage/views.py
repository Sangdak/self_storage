from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm, SignupForm
from app.storing.models import Client


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(username=cd['email'], password=cd['password'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                    return redirect(reverse('storing:myrent_page'))
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    context = {
        'form': form,
        'auth_switch': {
            'login_window': True,
        }
    }
    return render(request, '../templates/index.html', context)


def user_signup(request):
    form = SignupForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password1'] == cd['password2']:
                user = Client.objects.create_user(
                    username=cd['email'].split('@')[0],
                    first_name=cd['email'].split('@')[0],
                    email=cd['email'],
                    password=cd['password1'],
                )
                user.save()
                print(user.username)
                return redirect(reverse('login'))
    context = {
        'reg_form': form,
        'auth_switch': {
            'registration_window': True,
        }
    }
    return render(request, '../templates/index.html', context)


def user_logout(request):
    logout(request)
    return redirect(reverse('storing:main_page'))
