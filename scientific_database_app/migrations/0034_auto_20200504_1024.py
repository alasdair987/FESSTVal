# Generated by Django 3.0.4 on 2020-05-04 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0033_auto_20200429_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Timestamp'),
        ),
    ]
