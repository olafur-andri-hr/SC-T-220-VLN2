from django.db import models
from django.contrib.auth.models import User
from location.models import PostalCode
from phonenumber_field.modelfields import PhoneNumberField
from .validators import SSNValidator


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField()
    phone_number = PhoneNumberField(("Phone number"))
    postal_code = models.ForeignKey(
        PostalCode, verbose_name=("Postal Code"), on_delete=models.CASCADE
    )
    SSN = models.CharField(
        ("SSN"), max_length=15, validators=[SSNValidator(postal_code.country)]
    )
