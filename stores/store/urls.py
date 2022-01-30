from django.urls import path

from stores.store.views import index, create_store, update_store

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_store, name='create store'),
    path('edit/<int:pk>/', update_store, name='update store'),
]