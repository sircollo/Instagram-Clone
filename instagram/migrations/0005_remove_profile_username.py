# Generated by Django 4.0.4 on 2022-06-04 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_profile_username_alter_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
