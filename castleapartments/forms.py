from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import MinLengthValidator
from django.core.validators import validate_image_file_extension
from django.forms import ModelForm, DateInput, Textarea
from django_countries.fields import CountryField
from django.contrib.auth.forms import AuthenticationForm

from .models import User, UserInfo, CreditCard
from location.models import PostalCode
from apartments.models import ApartmentType


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
    min_price = forms.TypedChoiceField(
        label="Price (ISK):",
        required=False,
        choices=(
            [(i, str(i) + " million") for i in range(0, 101, 5)] +
            [(i, str(i) + " million") for i in range(110, 201, 10)] +
            [(j, str(j) + " million") for j in range(300, 1001, 100)]
        ),
        initial=0,
        widget=forms.Select(attrs={
            "placeholder": "Min",
            "class": "inline-first"
        }),
        coerce=int,
    )
    max_price = forms.TypedChoiceField(
        required=False,
        label="to",
        label_suffix="",
        choices=(
            [(i, str(i) + " million") for i in range(0, 101, 5)] +
            [(i, str(i) + " million") for i in range(110, 201, 10)] +
            [(j, str(j) + " million") for j in range(300, 1001, 100)]
        ),
        initial=1000,
        widget=forms.Select(attrs={
            "placeholder": "Max",
            "class": "inline-second",
        }),
        coerce=int,
    )
    min_size = forms.IntegerField(
        label="Size (m²):",
        required=False,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
        widget=forms.NumberInput(attrs={
            "placeholder": "Min",
            "class": "inline-first",
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
    per_page = forms.IntegerField(
        initial=3,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        widget=forms.HiddenInput(),
    )
    page_number = forms.IntegerField(
        initial=1,
        validators=[MinValueValidator(1)],
        widget=forms.HiddenInput(),
    )
    type = forms.ModelMultipleChoiceField(
        queryset=ApartmentType.objects.all(),
        required=False,
    )
    order_by = forms.ChoiceField(
        initial="-listing_date",
        label="Order by: ",
        choices=[("-listing_date", "Newest first"),
                 ("listing_date", "Oldest"),
                 ("apartment__appraisal", "Least expensive"),
                 ("-apartment__appraisal", "Most expensive"),
                 ("apartment__postal_code__zip_code", "Postal code"),
                 ("apartment__address", "Address"),
                 ],
        required=True,
        widget=forms.Select(attrs={"form": "search_banner_form"}),
    )


class OfferForm(forms.Form):
    offer_amount = forms.IntegerField(
        label="Offer amount:",
        required=True,
        widget=forms.NumberInput(attrs={
            "placeholder": "Appraisal",
            "class": ""
        })
    )
    conveyance_date = forms.DateField(
        label="Date of conveyance:",
        required=True,
        widget=forms.DateInput(attrs={
            "placeholder": "",
            "class": ""
        })
    )
    credit_card = CreditCard()


class SellForm(forms.Form):
    country = CountryField().formfield(attrs={
        "id": "countryInput"
    })
    zip_code = forms.CharField(
        label="Postal code", max_length=50, validators=[MinLengthValidator(2)]
    )
    town = forms.CharField(label=("Town"), max_length=50)
    address = forms.CharField(
        label="Address:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Address",
            "id": "addressInput"
        })
    )
    apt_number = forms.CharField(
        label="Apt. Number:",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Apt. Number",
            "id": "aptNumberInput"
        })
    )
    num_of_rooms = forms.IntegerField(
        label="Number of rooms:",
        required=True,
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        widget=forms.NumberInput(attrs={
            "placeholder": "# of rooms",
            "class": ""
        })
    )
    num_of_toilets = forms.IntegerField(
        label="Number of toilets:",
        required=True,
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        widget=forms.NumberInput(attrs={
            "placeholder": "# of toilets",
            "class": ""
        })
    )
    size = forms.FloatField(
        label="Size (m²):",
        required=True,
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(attrs={
            "placeholder": "Size",
            "class": ""
        })
    )
    type = forms.ModelChoiceField(
        queryset=ApartmentType.objects.all(),
        required=True,
    )
    description = forms.CharField(
        label="Detailed description:",
        required=True,
        widget=forms.Textarea(attrs={
            "placeholder": "Description",
            "class": "",
            "rows": "6",
            "id": "descriptionInput"
        })
    )
    appraisal = forms.IntegerField(
        label="Real estate appraisal amount:",
        required=True,
        widget=forms.NumberInput(attrs={
            "placeholder": "Appraisal",
            "class": ""
        })
    )
    year_built = forms.IntegerField(
        label="Year built:",
        required=True,
        widget=forms.NumberInput(attrs={
            "placeholder": "Year",
            "class": ""
        })
    )
    garage = forms.TypedChoiceField(
        label="Garage parking space:",
        required=True,
        widget=forms.RadioSelect(attrs={
            "class": "form-check-input",
        }),
        choices=((True, 'Yes'), (False, 'No')),
        initial=True,
        empty_value=None,
        coerce=bool
    )
    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        validators=[validate_image_file_extension],
        required=True
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
            postal_code.save()
        return postal_code


class UserInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        old = kwargs.get("old", None)
        super().__init__(*args, **kwargs)
        if old is not None:
            self.fields['profile_img'] = old.profile_img

    class Meta:
        model = UserInfo
        exclude = ('user', 'postal_code',)
        widgets = {
            'DoB': forms.DateInput(attrs={'placeholder': 'mm/dd/YYYY'}),
        }

    address = forms.CharField(
        label="Address:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Address"
        })
    )


class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        exclude = []
