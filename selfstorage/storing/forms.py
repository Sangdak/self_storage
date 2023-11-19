from django import forms
from .models import StoreHouse


class CalcForm(forms.Form):
    storehouse = forms.ModelChoiceField(queryset=StoreHouse.objects.all(), label='Склад')
    width = forms.DecimalField(label='Ширина, м')
    length = forms.DecimalField(label='Длина, м')
    height = forms.DecimalField(label='Высота, м')
