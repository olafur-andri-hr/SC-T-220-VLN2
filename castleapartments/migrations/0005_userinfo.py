# Generated by Django 2.2.1 on 2019-05-07 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0004_auto_20190507_1423'),
        ('castleapartments', '0004_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='First name')),
                ('last_name', models.CharField(max_length=20, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('profile_img', models.ImageField(upload_to='images/', verbose_name='Profile image')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('SSN', models.CharField(max_length=15, verbose_name='SSN')),
                ('DoB', models.DateField(verbose_name='Date of birth')),
                ('address', models.CharField(max_length=50, verbose_name='Home address')),
                ('apt_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Apt. number')),
                ('bio', models.TextField(max_length=300, verbose_name='Your bio')),
                ('postal_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.PostalCode', verbose_name='Postal Code')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
