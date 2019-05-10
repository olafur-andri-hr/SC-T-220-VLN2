from django.db import models

from django.core.validators import MinLengthValidator
from django_countries.fields import CountryField
# Create your models here.


class PostalCode(models.Model):
    zip_code = models.CharField(
        "Postal code", max_length=50,
        validators=[MinLengthValidator(2)]
    )
    country = CountryField()
    town = models.CharField(("City"), max_length=50)

    class Meta:
        unique_together = (('zip_code', 'country'),)

    def __str__(self):
        return f"{self.zip_code}, {self.country}"
