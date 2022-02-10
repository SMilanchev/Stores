from django.urls import path

from stores.store.views import IndexListView, StoreCreateView, StoreUpdateView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('create/', StoreCreateView.as_view(), name='create store'),
    path('edit/<int:pk>/', StoreUpdateView.as_view(), name='update store'),
]