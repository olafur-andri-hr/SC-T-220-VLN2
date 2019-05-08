from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import MinLengthValidator
from django.forms import ModelForm, DateInput, Textarea
from django_countries.fields import CountryField
from django.contrib.auth.forms import AuthenticationForm

from .models import User, UserInfo
from location.models import PostalCode


class SearchForm(forms.Form):
    address = forms.CharField(
        label="Address:",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "The property's address",
            "class": ""
        })
    )
    zip_code = forms.CharField(
        label="Zip code:",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "The property's zip code",
            "class": ""
        })
    )
    country = CountryField().formfield(
        label="Country:",
        required=False
    )
    town = forms.CharField(
        label="Town:",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "The property's town",
            "class": ""
        })
    )
    min_rooms = forms.IntegerField(
        label="Bedrooms",
        required=False,
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        widget=forms.NumberInput(attrs={
            "placeholder": "Min",
            "class": "inline-first"
        })
    )
    max_rooms = forms.IntegerField(
        required=False,
        label="to",
        label_suffix="",
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        widget=forms.NumberInput(attrs={
            "placeholder": "Max",
            "class": "inline-second"
        })
    )
    min_price = forms.ChoiceField(
        label="Price:",
        required=False,
        choices=[(str(i), str(i) + " million") for i in range(0, 201, 5)],
        initial="10",
        widget=forms.Select(attrs={
            "placeholder": "Min",
            "class": "inline-first"
        })
    )
    max_price = forms.ChoiceField(
        required=False,
        label="to",
        label_suffix="",
        choices=[(str(i), str(i) + " million") for i in range(0, 201, 5)],
        initial="100",
        widget=forms.Select(attrs={
            "placeholder": "Max",
            "class": "inline-second"
        })
    )
    min_size = forms.IntegerField(
        label="Size (m²):",
        required=False,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        widget=forms.NumberInput(attrs={
            "placeholder": "Min",
            "class": "inline-first"
        })
    )
    max_size = forms.IntegerField(
        required=False,
        label="to",
        label_suffix="",
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        widget=forms.NumberInput(attrs={
            "placeholder": "Max",
            "class": "inline-second"
        })
    )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label=("Email"), max_length=30)


class PostalCodeForm(forms.Form):
    zip_code = forms.CharField(
        label="Postal code", max_length=50, validators=[MinLengthValidator(2)]
    )
    country = CountryField().formfield()
    town = forms.CharField(label=("Town"), max_length=50)

    def get_postal_code(self):
        self.clean()
        zip_code = self.cleaned_data["zip_code"]
        country = self.cleaned_data["country"]
        town = self.cleaned_data["town"]
        try:
            postal_code = PostalCode.objects.get(
                zip_code=zip_code, country=country
            )
        except PostalCode.DoesNotExist:
            postal_code = PostalCode.objects.create(
                zip_code=zip_code, country=country, town=town
            )
            postal_code.save(commit=False)
        return postal_code


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('user', 'postal_code',)
        # fields = ('profile_img', 'phone_number', 'SSN', 'DoB',
        #           'postal_code', 'address', 'apt_number', 'bio',)
        widgets = {
            'DoB': forms.DateInput(attrs={'placeholder': 'mm/dd/YYYY'}),
        }

    # first_name = forms.CharField(
    #     label="First name:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your First name"
    #     })
    # )

    # last_name = forms.CharField(
    #     label="Last name:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your Last name"
    #     })
    # )

    # ssn = forms.CharField(
    #     label="SSN:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your SSN"
    #     })
    # )

    # dob = forms.CharField(
    #     label="Date of Birth:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your Date of birth"
    #     })
    # )

    # email = forms.EmailField(
    #     label="Email:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your Email"
    #     })
    # )

    # password = forms.CharField(
    #     label="Password:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your Password"
    #     })
    # )

    # country = forms.CharField(
    #     label="Country:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your country"
    #     })
    # )

    # zip_code = forms.CharField(
    #     label="Zip code:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your ZipCode"
    #     })
    # )

    # town = forms.CharField(
    #     label="Town:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your Town"
    #     })
    # )

    address = forms.CharField(
        label="Address:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Address"
        })
    )

    # aptN = forms.CharField(
    #     label="Apt. Number:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your Apt. Number"
    #     })
    # )

    # phone = forms.CharField(
    #     label="Phone:",
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(attrs={
    #         "placeholder": "Your Phone Number"
    #     })
    # )
