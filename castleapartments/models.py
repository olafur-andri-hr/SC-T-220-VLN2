from django.db import models
from django.forms import DateInput
from django.contrib.auth.models import User
from location.models import PostalCode
from phonenumber_field.modelfields import PhoneNumberField
from .validators import SSNValidator


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
