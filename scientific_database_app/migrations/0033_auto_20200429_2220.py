# Generated by Django 3.0.4 on 2020-04-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0032_auto_20200429_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='location_description',
            field=models.TextField(default=None),
        ),
    ]
