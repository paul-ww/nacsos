# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-09 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0072_runstats_dyn_win_threshold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runstats',
            name='dyn_win_threshold',
            field=models.FloatField(default=0.1),
        ),
    ]
