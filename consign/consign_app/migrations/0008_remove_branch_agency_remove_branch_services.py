# Generated by Django 5.0.6 on 2024-10-01 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0007_imageupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='services',
        ),
    ]
