# Generated by Django 2.2.2 on 2019-08-30 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20190830_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
    ]
