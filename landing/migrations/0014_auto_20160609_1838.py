# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-09 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_auto_20160606_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='building',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Квартира/Офис'),
        ),
        migrations.AlterField(
            model_name='order',
            name='house',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Дом/Корпус'),
        ),
    ]
