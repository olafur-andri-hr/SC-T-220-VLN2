from django import forms


class SearchForm(forms.Form):
    address = forms.CharField(
        label="Address:",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "The property's address"
        })
    )
    zip_code = forms.CharField(
        label="Zip code:",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "The property's zip code"
        })
    )
    country = forms.ChoiceField(
        label="Country:",
        required=False,
        choices=['Insert Django country dropdown here'],
        widget=forms.TextInput(attrs={
            "placeholder": "Select property's country"
        })
    )
    town = forms.CharField(
        label="Town:",
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "The property's town"
        })
    )
    rooms = forms.IntegerField(
        label="Num. of rooms:",
        required=False,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "min": "1",
            "max": "20",
            "step": "1"
        })
    )
    price = forms.IntegerField(
        label="Price:",
        required=False,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "min": "1000000",
            "max": "100000000",
            "step": "1"
        })
    )
    size = forms.IntegerField(
        label="Size:",
        required=False,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "min": "20",
            "max": "1000",
            "step": "1"
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
    firstName = forms.CharField(
        label="First name:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Your First name"
        })
    )  

    lastName = forms.CharField(
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

    