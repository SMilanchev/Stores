from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('stores.stores_auth.urls')),
    path('profile/', include('stores.profiles.urls')),
    path('common/', include('stores.common.urls')),
    path('', include('stores.store.urls')),
    path('location/', include('stores.location.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
