# Generated by Django 2.2.1 on 2019-05-11 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0004_auto_20190509_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='garage_parking_space',
            field=models.BooleanField(default=False, verbose_name='Garage parking space'),
        ),
    ]
