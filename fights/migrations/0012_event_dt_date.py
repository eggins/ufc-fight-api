# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-07 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fights', '0011_auto_20170130_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dt_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]