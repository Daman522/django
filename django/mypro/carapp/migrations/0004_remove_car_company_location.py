# Generated by Django 3.2.6 on 2021-08-19 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0003_car_company_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='company_location',
        ),
    ]
