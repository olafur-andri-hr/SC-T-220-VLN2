# Generated by Django 2.2.1 on 2019-05-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0007_auto_20190512_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sold_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date sold'),
        ),
    ]
