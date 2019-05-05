from django.db import models

from django.core.validators import MinLengthValidator
from django_countries.fields import CountryField
# Create your models here.


class PostalCode(models.Model):
    class Meta:
        unique_together = (('zip_code', 'country'),)
    zip_code = models.CharField(
        "Zip code", max_length=50, primary_key=True,
        validators=[MinLengthValidator(2)]
    )
    country = CountryField()
    town = models.CharField(("Town"), max_length=50)
