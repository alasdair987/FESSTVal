# Generated by Django 3.0.4 on 2020-04-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0030_auto_20200429_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='person_name',
            field=models.CharField(default=None, max_length=30, verbose_name='Name'),
        ),
    ]
