# Generated by Django 2.2.2 on 2021-03-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0338_auto_20210211_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='highlight',
            field=models.BooleanField(default=True),
        ),
    ]
