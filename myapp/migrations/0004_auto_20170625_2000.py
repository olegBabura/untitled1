# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170624_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='city',
            name='lon',
            field=models.FloatField(default=0),
        ),
    ]
