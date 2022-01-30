from django.core.exceptions import ValidationError


def capital_first_letter(value):
    if value[0].islower():
        raise ValidationError('First letter must be capital!')


def check_coordinates_numbers(value):
    try:
        value_list = value.split(', ')
        if len(value_list) <= 1 or len(value_list) >= 3:
            raise ValidationError('Values must be exactly 2 and separated by ", " ')
        list(map(float, value_list))
    except ValueError:
        raise ValidationError('Please enter numbers!')
