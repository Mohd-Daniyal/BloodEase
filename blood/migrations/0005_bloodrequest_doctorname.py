# Generated by Django 3.0.5 on 2023-10-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_bloodrequest_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='doctorname',
            field=models.CharField(default='dr', max_length=50),
            preserve_default=False,
        ),
    ]