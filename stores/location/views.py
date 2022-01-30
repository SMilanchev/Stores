from django.shortcuts import render
import folium
import geocoder
from stores.store.models import Store


def init_store_location_map(store_coordinates, store_name, initial_zoom):
    geocoder_loc = geocoder.osm(store_coordinates, method='reverse')
    store_popup = ", ".join([store_name, geocoder_loc.city, geocoder_loc.suburb, geocoder_loc.road])

    m = folium.Map(location=store_coordinates, zoom_start=initial_zoom)
    folium.Marker(store_coordinates, popup=store_popup, tooltip='Click for details').add_to(m)

    m = m._repr_html_()

    return m


def location_store(request, pk):
    store = Store.objects.get(pk=pk)
    store_coordinates = list(map(float, store.location.split(', ')))
    store_map = init_store_location_map(store_coordinates, store.name, 12)

    context = {
        'map': store_map,
        'store_name': store.name,
    }

    return render(request, 'location/location_store.html', context=context)