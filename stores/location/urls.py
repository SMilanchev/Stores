from django.urls import path

from stores.location.views import location_store

urlpatterns = [
    path('<int:pk>/', location_store, name='location store'),
]