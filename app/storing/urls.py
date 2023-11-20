from django.urls import path

from .views import *


app_name = "storing"

urlpatterns = [
    path('', mainpage, name='main_page'),
    path('faq/', faqpage, name='faq_page'),
    path('boxes/', boxespage, name='boxes_page'),
    path('my-rent/', myrentpage, name='myrent_page'),
    path('my-rent-empty/', myrentemptypage, name='myrentempty_page'),
    path('cost-calculation/', costcalculationpage, name='cost_calculation'),
]
