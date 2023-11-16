from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class StoreHouse(models.Model):
    title = models.CharField('Адрес', max_length=200)
    photo = models.ImageField('Фото')
    temperature = models.IntegerField('Температура')
    contacts = models.JSONField('Контакты')
    description = models.TextField('Описание')
    driveway = models.TextField('Схема проезда')

    def __str__(self):
        return self.title


class Box(models.Model):
    storehouse = models.ForeignKey(StoreHouse, on_delete=models.CASCADE, verbose_name='Склад')
    number = models.CharField('Номер', max_length=10)
    floor = models.IntegerField('Этаж')
    length = models.FloatField('Длина')
    width = models.FloatField('Ширина')
    height = models.FloatField('Высота')
    price = models.IntegerField('Цена')
    leaser = models.ForeignKey('UserProfile', verbose_name='Арендатор')
    lease_start = models.DateTimeField('Начало аренды', default=timezone.now)
    lease_finish = models.DateTimeField('Начало аренды', default=timezone.now)

    def __str__(self):
        return self.title


class Client(AbstractUser):
    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name='E-mail',
    )
    phone_number = PhoneNumberField(
        unique=True,
        blank=True,
        region='RU',
        verbose_name='Номер телефона'
    )
    image = models.ImageField(
        verbose_name='Аватар',
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} - {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
