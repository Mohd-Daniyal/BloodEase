# Generated by Django 3.0.5 on 2023-10-23 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0002_auto_20210213_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddonate',
            name='bloodgroup',
        ),
    ]