from django.core.exceptions import ValidationError


def capital_first_letter(value):
    if value[0].islower():
        raise ValidationError('First letter must be capital!')