# Generated by Django 2.2.1 on 2019-05-06 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20190505_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postalcode',
            name='zip_code',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Postal code'),
        ),
    ]
