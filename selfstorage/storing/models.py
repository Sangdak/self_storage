from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class StoreHouse(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название',
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес',
    )
    image = models.ImageField(
        verbose_name='Изображение',
    )
    store_class = models.CharField(
        max_length=2,
        default='D',
        verbose_name='Класс склада',
    )
    temperature = models.SmallIntegerField(
        default='N/A',
        verbose_name='Температура в складских помещениях',
    )
    contacts = models.CharField(
        max_length=150,
        blank=True,
        default='',
        verbose_name='Контакты',
    )
    description = models.TextField(
        blank=True,
        default='',
        verbose_name='Описание',
    )
    driveway_text = models.TextField(
        blank=True,
        default='',
        verbose_name='Схема проезда - текст',
    )
    driveway_image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Схема проезда - изображение',
    )

    def __str__(self):
        return f'{self.title}: {self.address}'

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class Box(models.Model):
    storehouse = models.ForeignKey(
        'StoreHouse',
        on_delete=models.CASCADE,
        verbose_name='Склад'
    )
    number = models.CharField(
        max_length=10,
        verbose_name='Номер бокса',
    )
    length = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Длина, м.',
    )
    width = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Ширина, м.',
    )
    height = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Высота, м.',
    )
    floor = models.SmallIntegerField(
        verbose_name='Этаж',
    )
    price = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name='Цена, руб',
    )

    def __str__(self):
        return f'№ {self.number} - {self.width}x{self.length}x{self.height}, склад: {self.storehouse.title}'

    class Meta:
        verbose_name = 'Бокс>'
        verbose_name_plural = 'Боксы'


class Lease(models.Model):
    leaser = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
        verbose_name='Арендатор',
    )
    box = models.ForeignKey(
        'Box',
        on_delete=models.PROTECT,
        verbose_name='Бокс'
    )
    lease_begin_datetime = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата/время начала срока аренды',
    )
    lease_end_datetime = models.DateTimeField(
        verbose_name='Дата/время завершения срока аренды',
    )

    def __str__(self):
        return (f'{self.lease_begin_datetime.date()}-{self.lease_end_datetime.date()} {self.box.number} - '
                f'{self.box.storehouse.title} - {self.leaser}')

    class Meta:
        verbose_name = 'Аренда бокса'
        verbose_name_plural = 'Аренда боксов'


class Client(AbstractUser):
    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name='E-mail',
    )
    phone_number = PhoneNumberField(
        # unique=True,
        blank=True,
        region='RU',
        verbose_name='Номер телефона'
    )
    image = models.ImageField(
        default='img/img1.png',
        verbose_name='Аватар',
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name} - {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
