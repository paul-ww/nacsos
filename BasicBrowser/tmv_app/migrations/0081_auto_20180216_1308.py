# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-16 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0080_auto_20180214_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamictopic',
            name='ipcc_score',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='dynamictopic',
            name='ipcc_share',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='dynamictopic',
            name='share',
            field=models.FloatField(null=True),
        ),
    ]