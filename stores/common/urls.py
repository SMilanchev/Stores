from django.urls import path

from stores.common.views import index, create_category, create_product

urlpatterns = [
    path('', index, name='index'),
    path('create-category', create_category, name='create category'),
    path('create-product', create_product, name='create product'),
]