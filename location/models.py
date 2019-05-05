from django.db import models

from django.core.validators import MinLengthValidator
from django_countries.fields import CountryField
# Create your models here.


class PostalCode(models.Model):
    zip_code = models.CharField("Zip code", max_length=50)
    country = CountryField()
    town = models.CharField(("Town"), max_length=50)
