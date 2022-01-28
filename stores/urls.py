from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('stores.stores_auth.urls')),
    path('profile/', include('stores.profiles.urls')),
    path('', include('stores.common.urls')),
]
