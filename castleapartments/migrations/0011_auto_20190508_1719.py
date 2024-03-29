# Generated by Django 2.2.1 on 2019-05-08 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('castleapartments', '0010_auto_20190508_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartmentimage',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='credit_card',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='listing',
        ),
        migrations.DeleteModel(
            name='Apartment',
        ),
        migrations.DeleteModel(
            name='ApartmentImage',
        ),
        migrations.DeleteModel(
            name='ApartmentType',
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
    ]
