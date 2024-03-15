# Generated by Django 3.0.4 on 2020-03-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_database_app', '0015_auto_20200307_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='Condition after maintenance',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='Condition before maintenance',
        ),
        migrations.RemoveField(
            model_name='maintenance',
            name='On-site maintenance?',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='choice1',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='No', max_length=30, verbose_name='On-site maintenance?'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='choice2',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('malfunction', 'Malfunction')], default='Active', max_length=30, verbose_name='Condition before maintenance'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='choice3',
            field=models.CharField(choices=[('active', 'Active'), ('active_with_problems', 'Active with Problems'), ('inactive', 'Inactive')], default='Active', max_length=30, verbose_name='Condition after maintenance'),
        ),
    ]
