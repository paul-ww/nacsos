# Generated by Django 2.2 on 2019-10-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parliament', '0051_auto_20190703_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='aph_id',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='unique_id',
            field=models.TextField(null=True),
        ),
    ]