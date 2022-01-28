from django.urls import path

from stores.common.views import index

urlpatterns = [
    path('', index, name='index')
]