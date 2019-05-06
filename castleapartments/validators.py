from django.forms import ValidationError


class SSNValidator():
    def __init__(self, country: str):
        self.country = str(country)

    def __call__(self, value):
        if self.country.capitalize() == 'IS':
            self.kennitala(value)

    def kennitala(self, kennitala):
        personal_id_number = personal_id_number.strip()
        personal_id_number = personal_id_number.replace("-", "")
        personal_id_number = personal_id_number.replace(" ", "")
        if not (9 <= len(personal_id_number) <= 10):
            raise ValidationError("Invalid kennitala")
