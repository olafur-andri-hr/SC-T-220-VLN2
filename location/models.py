from django.db import models

from django.core.validators import MinLengthValidator
# Create your models here.


class Country(models.Model):
    country_name = models.CharField("Country", max_length=50)
    country_code = models.CharField(
        "ISO", max_length=2, primary_key=True,
        validators=[MinLengthValidator(2)]
    )
    flag_emoji = models.CharField(("Flag Emoji"), max_length=1, unique=True)
    calling_code = models.CharField(
        ("Calling code"), max_length=4, unique=True
    )


class PostalCode(models.Model):
    zip_code = models.CharField("Zip code", max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    town = models.CharField(("Town"), max_length=50)
