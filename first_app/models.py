from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Color(models.Model):
    color = models.CharField(max_length=20, unique=True,
                             validators=[MinLengthValidator(3)])

    def __str__(self):
        return str(self.color).capitalize()

    def save(self, *args, **kwargs):
        self.color = str(self.color).capitalize()
        super().save(*args, **kwargs)


class Vehicle(models.Model):
    license_plate = models.CharField(primary_key=True, max_length=5)
    wheel_count = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING)


class Car(Vehicle):
    manufacturer = models.CharField(max_length=30)


class Scooter(Vehicle):
    cc = models.FloatField()


class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(
        max_length=2, primary_key=True, validators=[MinLengthValidator(2)]
    )


class Town(models.Model):
    town = models.CharField(max_length=50)


class Zip(models.Model):
    zip_code = models.CharField("Zip code", max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.DO_NOTHING)


class User(models.Model):
    ssn = models.CharField(("SSN"), max_length=50, primary_key=True)
    name = models.CharField(("Name"), max_length=50)
    image = models.ImageField(
        ("Profile image"), upload_to='images/', height_field=None,
        width_field=None, max_length=None
    )
    favorite_color = models.CharField(
        ("Favorite color"), max_length=50, default="red")
