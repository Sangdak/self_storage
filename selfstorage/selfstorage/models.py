from django.db import models
from django.conf import settings
from django.utils import timezone


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


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.TextField()
    phone = models.CharField()
    email = models.EmailField()
    photo = models.ImageField()

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

