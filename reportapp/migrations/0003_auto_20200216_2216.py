# Generated by Django 3.0.2 on 2020-02-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportapp', '0002_report_time_of_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_of_report',
            field=models.CharField(choices=[(1, 'Icyumweru'), (2, 'Ukwezi'), (3, 'Igihembwe'), (4, 'Amezi atandatu'), (5, 'Umwaka')], max_length=50),
        ),
    ]
