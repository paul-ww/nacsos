# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0022_auto_20170803_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='runstats',
            name='parent_run_id',
            field=models.IntegerField(null=True),
        ),
    ]
