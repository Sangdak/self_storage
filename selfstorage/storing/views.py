from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count, Min, Max
from django.utils.timezone import localtime
from .models import StoreHouse, Box, Lease


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
    now = localtime()
    all_storehouses = StoreHouse.objects.all()
    for storehouse in all_storehouses:
        storehouse.boxes_count = storehouse.boxes.count()
        storehouse.minimal_price = storehouse.boxes.aggregate(Min('price'))
        storehouse.max_ceiling_height = storehouse.boxes.aggregate(Max('height'))

        all_boxes = storehouse.boxes.all()
        boxes_ids = [box.id for box in all_boxes]
        leased_boxes = Lease.objects.filter(box__in=boxes_ids).filter(lease_end_datetime__gt=now).count()
        storehouse.free_boxes = storehouse.boxes_count - leased_boxes

    context = {
        'all_storehouses': all_storehouses,
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
