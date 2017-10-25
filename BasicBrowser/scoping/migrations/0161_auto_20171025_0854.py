# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-25 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmv_app', '0045_auto_20171025_0854'),
        ('scoping', '0160_auto_20171024_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bibcouple',
            name='doc1',
        ),
        migrations.RemoveField(
            model_name='bibcouple',
            name='doc2',
        ),
        migrations.RemoveField(
            model_name='cdo',
            name='citation',
        ),
        migrations.RemoveField(
            model_name='cdo',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='citation',
            name='referent',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='category',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='cities',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='innovation',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='query',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='references',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='uploader',
        ),
        migrations.RemoveField(
            model_name='doc',
            name='users',
        ),
        migrations.AlterUniqueTogether(
            name='docauthinst',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='docauthinst',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='docbigram',
            name='bigram',
        ),
        migrations.RemoveField(
            model_name='docbigram',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='docownership',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='docownership',
            name='query',
        ),
        migrations.RemoveField(
            model_name='docownership',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='docownership',
            name='user',
        ),
        migrations.RemoveField(
            model_name='docproject',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='docproject',
            name='project',
        ),
        migrations.RemoveField(
            model_name='docreferences',
            name='doc',
        ),
        migrations.AlterUniqueTogether(
            name='docrel',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='docrel',
            name='referent',
        ),
        migrations.RemoveField(
            model_name='docrel',
            name='seed',
        ),
        migrations.RemoveField(
            model_name='docrel',
            name='seedquery',
        ),
        migrations.RemoveField(
            model_name='ipccref',
            name='ar',
        ),
        migrations.RemoveField(
            model_name='ipccref',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='ipccref',
            name='wg',
        ),
        migrations.RemoveField(
            model_name='kw',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='networkproperties',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='networkproperties',
            name='network',
        ),
        migrations.RemoveField(
            model_name='note',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wc',
            name='doc',
        ),
        migrations.RemoveField(
            model_name='wosarticle',
            name='doc',
        ),
        migrations.AlterField(
            model_name='bibcouple_copy',
            name='cocites',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='BibCouple',
        ),
        migrations.DeleteModel(
            name='CDO',
        ),
        migrations.DeleteModel(
            name='Citation',
        ),
        migrations.DeleteModel(
            name='Doc',
        ),
        migrations.DeleteModel(
            name='DocAuthInst',
        ),
        migrations.DeleteModel(
            name='DocBigram',
        ),
        migrations.DeleteModel(
            name='DocOwnership',
        ),
        migrations.DeleteModel(
            name='DocProject',
        ),
        migrations.DeleteModel(
            name='DocReferences',
        ),
        migrations.DeleteModel(
            name='DocRel',
        ),
        migrations.DeleteModel(
            name='IPCCRef',
        ),
        migrations.DeleteModel(
            name='KW',
        ),
        migrations.DeleteModel(
            name='NetworkProperties',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='WC',
        ),
        migrations.DeleteModel(
            name='WoSArticle',
        ),
    ]
