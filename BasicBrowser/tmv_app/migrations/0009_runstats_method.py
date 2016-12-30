# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0008_runstats_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='runstats',
            name='method',
            field=models.CharField(choices=[('LD', 'lda'), ('HL', 'hlda'), ('DT', 'dtm')], default='LD', max_length=2),
        ),
    ]