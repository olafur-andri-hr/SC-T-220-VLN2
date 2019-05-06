from django import forms


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
    country = forms.ChoiceField(
        label="Country:",
        required=False,
        choices=['Insert Django country dropdown here'],
        widget=forms.TextInput(attrs={
            "placeholder": "Select property's country",
            "class": ""
        })
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
        label="Rooms (min, max):",
        required=False,
        widget=forms.NumberInput(attrs={
            "placeholder": "Min rooms",
            "class": "inline-first"
        })
    )
    max_rooms = forms.IntegerField(
        required=False,
        label="",
        widget=forms.NumberInput(attrs={
            "placeholder": "Max rooms",
            "class": "inline-second"
        })
    )
    price = forms.IntegerField(
        label="Price:",
        required=False,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "min": "1000000",
            "max": "100000000",
            "step": "1",
            "class": ""
        })
    )
    size = forms.IntegerField(
        label="Size:",
        required=False,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "min": "20",
            "max": "1000",
            "step": "1",
            "class": ""
        })
    )


class LoginForm(forms.Form):
    email = forms.CharField(
        label="Email:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Email"
        })
    )    
    password = forms.CharField(
        label="Password:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Password"
        })
    )


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        label="First name:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your First name"
        })
    )  

    last_name = forms.CharField(
        label="Last name:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Last name"
        })
    )

    ssn = forms.CharField(
        label="SSN:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your SSN"
        })
    )

    dob = forms.CharField(
        label="Date of Birth:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Date of birth"
        })
    )

    email = forms.CharField(
        label="Email:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Email"
        })
    )

    password = forms.CharField(
        label="Password:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Password"
        })
    )

    country = forms.CharField(
        label="Country:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your country"
        })
    )  

    zip_code = forms.CharField(
        label="Zip code:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your ZipCode"
        })
    )

    town = forms.CharField(
        label="Town:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Town"
        })
    )

    address = forms.CharField(
        label="Address:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Address"
        })
    )

    aptN = forms.CharField(
        label="Apt. Number:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Apt. Number"
        })
    )

    phone = forms.CharField(
        label="Phone:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your Phone Number"
        })
    )
    