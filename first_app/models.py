from django.db import models

# Create your models here.


class Color(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return str(self.color).capitalize()

    def save(self, *args, **kwargs):
        self.color = str(self.color).capitalize()
        super().save(*args, **kwargs)


class Vehicle(models.Model):
    license_plate = models.CharField(primary_key=True, max_length=5)
    wheel_count = models.IntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)


class Car(Vehicle):
    manufacturer = models.CharField(max_length=30)


class Scooter(Vehicle):
    cc = models.FloatField()
