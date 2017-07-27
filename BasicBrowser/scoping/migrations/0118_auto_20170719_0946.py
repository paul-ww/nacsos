# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-19 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0117_bigram_docbigram'),
    ]

    operations = [
        migrations.AddField(
            model_name='citation',
            name='docmatches',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='citation',
            name='referent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc'),
        ),
    ]