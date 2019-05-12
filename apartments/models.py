import uuid
from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


# Create your models here.


class ApartmentType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return str(self.name)


class Apartment(models.Model):
    postal_code = models.ForeignKey(
        "location.PostalCode", verbose_name=("Postal code"),
        on_delete=models.CASCADE
    )
    address = models.CharField(("Address"), max_length=50)
    apt_number = models.CharField(
        ("Apt. number"), max_length=50, null=True, blank=True
    )
    appraisal = models.BigIntegerField(("Appraisal"))
    num_rooms = models.IntegerField(("Bedrooms"))
    num_bathrooms = models.IntegerField(("Bathrooms"))
    size = models.FloatField(("Size (m²)"))
    apartment_type = models.ForeignKey(
        ApartmentType, verbose_name=("Apartment type"),
        on_delete=models.CASCADE
    )
    description = models.TextField(("Description"))
    description_truncation_length = models.IntegerField(default=100)
    garage_parking_space = models.BooleanField(
        ("Garage parking space"), default=False
    )
    year_built = models.IntegerField(("Year built"), default=0)

    def __str__(self):
        return (f"{self.address}, {self.postal_code}")


class ApartmentImage(models.Model):
    # image = models.ImageField(
    #     ("Image"), upload_to="apartments/", height_field=None,
    #     width_field=None, max_length=None
    # )
    image = ProcessedImageField(
        verbose_name=("Image"),
        upload_to='apartments/',
        processors=[ResizeToFit(1024, 1024)],
        format='JPEG',
        options={'quality': 60}
    )
    apartment = models.ForeignKey(
        Apartment, verbose_name=("Apartment Image"),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.image.url)


class Listing(models.Model):
    uuid = models.UUIDField(
        ("uuid"), primary_key=True, default=uuid.uuid4, editable=False
    )
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    seller = models.ForeignKey(
        User, verbose_name=("Seller"), on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    listing_date = models.DateTimeField(
        ("Listing date"), auto_now=True, auto_now_add=False
    )
    sold_date = models.DateField(
        ("Date sold"), auto_now=False, auto_now_add=False,
        null=True, blank=True
    )
    processed = models.BooleanField(("Processed by staff"), default=False)

    def __str__(self):
        return f"{self.seller}: {self.apartment}"
