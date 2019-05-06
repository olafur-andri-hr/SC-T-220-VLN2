from django.db import models
from django.contrib.auth.models import User
from location.models import PostalCode
from phonenumber_field.modelfields import PhoneNumberField
from .validators import SSNValidator


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField()
    phone_number = PhoneNumberField(("Phone number"))
    SSN = models.CharField(("SSN"), max_length=15)
    DoB = models.DateField(
        ("Date of birth"), auto_now=False, auto_now_add=False
    )
    postal_code = models.ForeignKey(
        PostalCode, verbose_name=("Postal Code"), on_delete=models.CASCADE
    )
    address = models.CharField(("Home address"), max_length=50)
    apartment_num = models.CharField(("Apt. number"), max_length=50)
    bio = models.TextField(("Your bio"))
