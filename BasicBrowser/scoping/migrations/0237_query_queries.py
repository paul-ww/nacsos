# Generated by Django 2.0.5 on 2018-10-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0236_auto_20181004_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='queries',
            field=models.ManyToManyField(to='scoping.Query'),
        ),
    ]