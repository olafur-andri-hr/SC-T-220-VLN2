from django.db import models
from django.forms import DateInput
from django.contrib.auth.models import User
from location.models import PostalCode
from phonenumber_field.modelfields import PhoneNumberField
from .validators import SSNValidator, credit_card_validator
from apartments.models import Apartment, ApartmentType, ApartmentImage
from apartments.models import Listing
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(("First name"), max_length=20)
    last_name = models.CharField(("Last name"), max_length=20)
    email = models.EmailField(("Email"), max_length=254)
    profile_img = ProcessedImageField(
        verbose_name=("Image"),
        upload_to='images/',
        processors=[ResizeToFit(1024, 1024)],
        format='JPEG',
        options={'quality': 80}
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

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


class CreditCard(models.Model):
    credit_card_number = models.CharField(
        max_length=22, validators=[credit_card_validator]
    )
    credit_card_expiration_date = models.DateField(
        ("Expiration date"), auto_now=False, auto_now_add=False
    )
    credit_card_cvv = models.CharField(("CVV"), max_length=4)

    def __str__(self):
        return str(self.credit_card_number)


class Offer(models.Model):
    buyer = models.ForeignKey(
        User, verbose_name=("Buyer"), on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    listing = models.ForeignKey(
        "apartments.Listing", verbose_name=("Listing"),
        on_delete=models.CASCADE
    )
    request_date = models.DateTimeField(
        ("Offer request date"), auto_now=True, auto_now_add=False
    )
    request_amount = models.IntegerField(("Offer request amount"))
    credit_card = models.OneToOneField(
        CreditCard, verbose_name=("Credit card"), on_delete=models.CASCADE,
        null=True, blank=True
    )
    accepted = models.BooleanField(("Accepted"), default=False)
    processed = models.BooleanField(("Processed by staff"), default=False)

    class Meta:
        unique_together = (('buyer', 'listing'),)

    def __str__(self):
        return f'{self.buyer} offers {self.listing}'
