# Generated by Django 2.1.2 on 2018-11-22 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0013_user_scrape_fetched'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='since',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='until',
            field=models.DateTimeField(null=True),
        ),
    ]
