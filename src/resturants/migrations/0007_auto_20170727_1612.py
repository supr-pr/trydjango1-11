# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0006_resturant_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resturant',
            old_name='categories',
            new_name='category',
        ),
    ]
