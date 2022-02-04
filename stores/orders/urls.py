from django.urls import path

from stores.orders.views import add_to_order, send_order

urlpatterns = [
    path('add-product/<int:pk>/', add_to_order, name='add to order'),
    path('send_order', send_order, name='send order'),
]