# Generated by Django 3.0.4 on 2020-04-29 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0020_auto_20200429_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='choice4',
            field=models.CharField(choices=[('not affected', 'Not Affected'), ('maybe affected', 'Maybe Affected'), ('affected', 'Affected')], default='Not affected', max_length=30, verbose_name='Homogeneity'),
        ),
    ]