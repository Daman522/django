# Generated by Django 3.2.7 on 2021-09-23 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myappp', '0008_rename_forgetpassword_forgetpassword2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forgetpassword2',
            name='forget_password_token',
        ),
        migrations.RemoveField(
            model_name='forgetpassword2',
            name='url_path',
        ),
    ]
