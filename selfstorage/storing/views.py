from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def mainpage(request):
    context = {
        'key': 'value',
    }
    return render(request, 'index.html', context)


def faqpage(request):
    context = {
        'key': 'value',
    }
    return render(request, 'faq.html', context)


def boxespage(request):
    context = {
        'key': 'value',
    }
    return render(request, 'boxes.html', context)


@login_required(login_url='accounts/login/')
def myrentpage(request):
    context = {
        'key': 'value',
    }
    print(request.user.last_name)
    return render(request, 'my-rent.html', context)


def myrentemptypage(request):
    context = {
        'key': 'value',
    }
    return render(request, 'my-rent-empty.html', context)
