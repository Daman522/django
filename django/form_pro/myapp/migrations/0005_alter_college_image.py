# Generated by Django 3.2.7 on 2021-10-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_college_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
