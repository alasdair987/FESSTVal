# Generated by Django 3.0.4 on 2020-04-29 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0023_auto_20200429_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='person_name',
            field=models.CharField(default='', max_length=30, verbose_name='Type your Name'),
        ),
    ]