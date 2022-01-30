import geocoder
from django.core.exceptions import ValidationError


def check_coordinates_valid(value):
    try:
        coordinates = value.split(', ')
        geo_loc = geocoder.osm(coordinates, method='reverse')
        if not geo_loc:
            raise ValidationError('Cannot find such place!')
    except ValueError as exc:
        raise ValidationError(exc)
