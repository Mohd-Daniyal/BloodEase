# Generated by Django 3.0.5 on 2023-10-23 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0006_auto_20231021_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloodrequest',
            name='request_by_donor',
        ),
    ]
