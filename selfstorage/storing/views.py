from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count, Min, Max
from django.utils.timezone import localtime
from .models import StoreHouse, Box, Lease
from .forms import CalcForm


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


# def boxespage(request):
#     now = localtime()
#     all_storehouses = StoreHouse.objects.all()
#     for storehouse in all_storehouses:
#         storehouse.boxes_count = storehouse.boxes.count()
#         storehouse.minimal_price = storehouse.boxes.aggregate(Min('price'))
#         storehouse.max_ceiling_height = storehouse.boxes.aggregate(Max('height'))
#
#         all_boxes = storehouse.boxes.all()
#         boxes_ids = [box.id for box in all_boxes]
#         leased_boxes = Lease.objects.filter(box__in=boxes_ids).filter(lease_end_datetime__gt=now).count()
#         storehouse.free_boxes = storehouse.boxes_count - leased_boxes
#
#     context = {
#         'all_storehouses': all_storehouses,
#     }
#     return render(request, 'boxes.html', context)


def boxespage(request):
    now = localtime()
    storehouses = StoreHouse.objects.all()
    for storehouse in storehouses:
        storehouse_boxes = storehouse.boxes.all()
        leased_boxes_number = (Lease.objects.filter(box__storehouse__id=storehouse.id)
                               .filter(lease_end_datetime__gte=now).count())

        storehouse.boxes_number = storehouse_boxes.count()
        storehouse.box_minimal_price = storehouse.boxes.aggregate(Min('price'))
        storehouse.box_max_height = storehouse.boxes.aggregate(Max('height'))
        storehouse.free_boxes_number = storehouse.boxes_number - leased_boxes_number

    context = {
        'storehouses': storehouses,
    }

    return render(request, 'boxes.html', context)


@login_required(login_url='accounts/login/')
def myrentpage(request):
    user_boxes = Lease.objects.filter(leaser__id=request.user.id)

    context = {
        'boxes': user_boxes,
    }

    return render(request, 'my-rent.html', context)


def myrentemptypage(request):
    context = {
        'key': 'value',
    }
    return render(request, 'my-rent-empty.html', context)


def costcalculationpage(request):
    now = localtime()
    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            storehouse = cd['storehouse']
            cargo_width = cd['width']
            cargo_length = cd['length']
            cargo_height = cd['height']

            storehouse_boxes = storehouse.boxes.all()
            active_leases = Lease.objects.filter(box__storehouse__id=storehouse.id).filter(lease_end_datetime__gte=now)
            leased_boxes = [lease.box.id for lease in active_leases]
            free_boxes = storehouse_boxes.exclude(id__in=leased_boxes)
            fit_free_boxes = free_boxes.filter(length__gte=cargo_length, width__gte=cargo_width, height__gte=cargo_height).order_by('price')

            if fit_free_boxes:
                fit_free_box = fit_free_boxes[0]
                box = f'Вам подойдет бокс {fit_free_box} за {fit_free_box.price} рублей.'
            else:
                box = f'К сожалению, подходящих для Вас боксов на складе {storehouse} не нашлось.'

        context = {
            'form': form,
            'box': box,
            }

        return render(request, 'cost-calculation.html', context)

    else:
        form = CalcForm()
        context = {
            'form': form,
        }
        return render(request, 'cost-calculation.html', context)
