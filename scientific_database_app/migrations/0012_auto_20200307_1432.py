# Generated by Django 3.0.4 on 2020-03-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0011_auto_20200306_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='description',
            field=models.TextField(default='Type your Description in here.'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='timestamp',
            field=models.DateField(),
        ),
    ]
