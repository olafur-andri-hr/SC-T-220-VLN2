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


def credit_card_validator(ccn):
    ccn = ccn.strip().replace("-", "").replace(" ", "")
    # Uses modified https://en.wikipedia.org/wiki/Luhn_algorithm
    # to check credit card validity
    LUHN_ODD_LOOKUP = (0, 2, 4, 6, 8,
                       1, 3, 5, 7, 9)  # sum_of_digits (index * 2)
    try:
        evens = sum(int(p) for p in ccn[-1::-2])
        odds = sum(LUHN_ODD_LOOKUP[int(p)] for p in ccn[-2::-2])
        if (evens + odds) % 10 == 0:
            return ccn
    except ValueError:  # Raised if an int conversion fails
        pass
    raise ValidationError("Invalid credit card number.")
