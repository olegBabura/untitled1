# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170626_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
