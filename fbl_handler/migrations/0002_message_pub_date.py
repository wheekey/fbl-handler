# Generated by Django 3.0.6 on 2020-05-19 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbl_handler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
