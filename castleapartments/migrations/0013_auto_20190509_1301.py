# Generated by Django 2.2.1 on 2019-05-09 13:01

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('castleapartments', '0012_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='profile_img',
            field=imagekit.models.fields.ProcessedImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]
