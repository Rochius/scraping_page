# Generated by Django 4.1.3 on 2022-11-23 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0005_search_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='dateInput',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 12, 17, 14, 646908)),
        ),
    ]
