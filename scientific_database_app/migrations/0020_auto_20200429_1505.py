# Generated by Django 3.0.4 on 2020-04-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0019_auto_20200429_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='person_name',
            field=models.CharField(default='Name', max_length=30, verbose_name='Type your Name here'),
        ),
    ]
