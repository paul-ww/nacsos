# Generated by Django 2.2.2 on 2020-01-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0312_auto_20200113_1702'),
        ('twitter', '0018_searchprogress'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='tag',
            field=models.ManyToManyField(to='scoping.Tag'),
        ),
    ]