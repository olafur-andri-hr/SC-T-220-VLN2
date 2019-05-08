from django.db import models
from django.forms import DateInput
from django.contrib.auth.models import User
from location.models import PostalCode
from phonenumber_field.modelfields import PhoneNumberField
from .validators import SSNValidator, credit_card_validator


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(("First name"), max_length=20)
    last_name = models.CharField(("Last name"), max_length=20)
    email = models.EmailField(("Email"), max_length=254)
    profile_img = models.ImageField(
        ("Profile image"), upload_to='images/', height_field=None,
        width_field=None, max_length=None
    )
    phone_number = PhoneNumberField(("Phone number"))
    SSN = models.CharField(("SSN"), max_length=15)
    DoB = models.DateField(
        ("Date of birth"), auto_now=False, auto_now_add=False
    )
    postal_code = models.ForeignKey(
        PostalCode, verbose_name=("Postal Code"), on_delete=models.CASCADE
    )
    address = models.CharField(("Home address"), max_length=50)
    apt_number = models.CharField(
        ("Apt. number"), max_length=50, null=True, blank=True
    )
    bio = models.TextField(("Your bio"), max_length=300)


class ApartmentType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=300)

    def __str__(self):
        return str(self.name)


class Apartment(models.Model):
    postal_code = models.ForeignKey(
        PostalCode, verbose_name=("Postal code"), on_delete=models.CASCADE
    )
    address = models.CharField(("Address"), max_length=50)
    apt_number = models.CharField(
        ("Apt. number"), max_length=50, null=True, blank=True
    )
    appraisal = models.BigIntegerField(("Appraisal"))
    num_rooms = models.IntegerField(("Bedrooms"))
    num_bathrooms = models.IntegerField(("Bathrooms"))
    size = models.IntegerField(("Size (m²)"))
    apartment_type = models.ForeignKey(
        ApartmentType, verbose_name=("Apartment type"),
        on_delete=models.CASCADE
    )
    description = models.TextField(("Description"))


class ApartmentImage(models.Model):
    image = models.ImageField(
        ("Image"), upload_to="apartments/", height_field=None,
        width_field=None, max_length=None
    )
    apartment = models.ForeignKey(
        Apartment, verbose_name=(""), on_delete=models.CASCADE
    )


class Listing(models.Model):
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


class CreditCard(models.Model):
    credit_card_number = models.CharField(
        max_length=22, validators=[credit_card_validator],
    )
    credit_card_expiration_date = models.DateField(
        ("Expiration date"), auto_now=False, auto_now_add=False
    )
    credit_card_cvv = models.CharField(("CVV"), max_length=4)


class Offer(models.Model):
    buyer = models.ForeignKey(
        User, verbose_name=("Buyer"), on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    listing = models.ForeignKey(
        Listing, verbose_name=("Listing"),
        on_delete=models.CASCADE
    )
    request_date = models.DateTimeField(
        ("Offer request date"), auto_now=True, auto_now_add=False
    )
    request_amount = models.IntegerField(("Offer request amount"))
    credit_card = models.OneToOneField(
        CreditCard, verbose_name=(""), on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    accepted = models.BooleanField(("Accepted"), default=False)
    processed = models.BooleanField(("Processed by staff"), default=False)
