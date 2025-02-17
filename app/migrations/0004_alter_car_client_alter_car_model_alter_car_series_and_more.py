# Generated by Django 5.1.4 on 2025-01-08 17:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_servicerecord_order_rename_make_car_series_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to=settings.AUTH_USER_MODEL, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=100, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='series',
            field=models.CharField(max_length=100, verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='order',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_records', to='app.car', verbose_name='Машина'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='order',
            name='service_date',
            field=models.DateField(verbose_name='Дата обслуживания'),
        ),
    ]
