from django.urls import path

from stores.common.views import create_category, create_product, update_product, update_category, delete_product, \
    delete_category, list_category

urlpatterns = [
    path('create-category/', create_category, name='create category'),
    path('update-category/<int:pk>/', update_category, name='update category'),
    path('delete-category/<int:pk>/', delete_category, name='delete category'),
    path('create-product/', create_product, name='create product'),
    path('update-product/<int:pk>/', update_product, name='update product'),
    path('delete-product/<int:pk>/', delete_product, name='delete product'),
    path('list-category/<int:pk>', list_category, name='list category'),
]