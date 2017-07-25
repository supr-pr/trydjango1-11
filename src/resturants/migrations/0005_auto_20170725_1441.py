# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0004_resturant_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturant',
            name='my_date_field',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='resturant',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='resturant',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]