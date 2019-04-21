from django.db import models

# Create your models here.


class Color(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"str: {self.color}"

    def __unicode__(self):
        return f"unicode: {self.color}"

    def __repr__(self):
        return f"repr: {self.color}"


class Vehicle(models.Model):
    license_plate = models.CharField(primary_key=True, max_length=5)
    wheel_count = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)


class Car(Vehicle):
    manufacturer = models.CharField(max_length=30)


class Scooter(Vehicle):
    cc = models.FloatField()
