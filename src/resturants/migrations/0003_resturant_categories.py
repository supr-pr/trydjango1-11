# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0002_resturant_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturant',
            name='categories',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]