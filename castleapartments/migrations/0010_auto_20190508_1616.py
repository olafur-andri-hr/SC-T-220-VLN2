# Generated by Django 2.2.1 on 2019-05-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('castleapartments', '0009_auto_20190507_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='size',
            field=models.FloatField(verbose_name='Size (m²)'),
        ),
    ]
