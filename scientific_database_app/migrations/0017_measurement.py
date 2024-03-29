# Generated by Django 3.0.4 on 2020-03-07 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0016_auto_20200307_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_name', models.CharField(max_length=30)),
                ('measurement_description', models.TextField(default='Type your Description in here.')),
                ('location_description', models.TextField(default='Type your Description in here.')),
                ('position', models.CharField(max_length=30)),
                ('files', models.FileField(blank=True, null=True, upload_to='')),
                ('networks', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='scientific_database_app.Networks')),
            ],
        ),
    ]
