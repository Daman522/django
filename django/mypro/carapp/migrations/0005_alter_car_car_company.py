# Generated by Django 3.2.6 on 2021-08-19 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_remove_car_company_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='car', to='carapp.company'),
        ),
    ]