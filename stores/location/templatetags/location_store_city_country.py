from django.template import Library
import geocoder

register = Library()


@register.simple_tag
def get_store_city_and_country(coordinates):
    store_coordinates = list(map(float, coordinates.split(', ')))
    place = geocoder.osm(store_coordinates, method='reverse')
    return place.address
