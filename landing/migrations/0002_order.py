# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-04 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200, verbose_name='Имя')),
                ('street', models.CharField(blank=True, default='', max_length=200, verbose_name='Улица')),
                ('house', models.CharField(blank=True, default='', max_length=200, verbose_name='Дом')),
                ('corps', models.CharField(blank=True, default='', max_length=200, verbose_name='Корпус')),
                ('building', models.CharField(blank=True, default='', max_length=200, verbose_name='Строение')),
                ('number', models.CharField(blank=True, default='', max_length=200, verbose_name='NO(Номер)')),
                ('phone', models.CharField(blank=True, default='', max_length=200, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, default='', max_length=200, verbose_name='E-mail')),
                ('company', models.CharField(blank=True, default='', max_length=200, verbose_name='Название компании')),
            ],
        ),
    ]
