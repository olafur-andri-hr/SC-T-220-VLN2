# Generated by Django 2.2.1 on 2019-05-07 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('castleapartments', '0007_auto_20190507_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentimage',
            name='apartment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='castleapartments.Apartment', verbose_name=''),
        ),
    ]