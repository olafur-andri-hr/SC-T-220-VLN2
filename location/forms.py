from django.forms import ModelForm
from .models import PostalCode


class PostalCodeForm(ModelForm):
    class Meta:
        model = PostalCode
        exclude = []
