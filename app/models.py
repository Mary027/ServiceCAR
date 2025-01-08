# Импорт модуля models из библиотеки Django
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Guest'),
        ('registered', 'Registered'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')

class Car(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars', verbose_name='Клиент')
    model = models.CharField(max_length=100, verbose_name='Модель')
    series = models.CharField(max_length=100, verbose_name='Серия')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')

    def __str__(self):
        return f'{self.model} ({self.series})'

class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='service_records', verbose_name='Машина')
    service_date = models.DateField(verbose_name='Дата обслуживания')
    description = models.TextField(verbose_name='Описание')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.car} - {self.service_date}'