from django.urls import path

from stores.common.views import update_product, delete_product, \
    delete_category, ProductCreateView, CategoryCreateView, CategoryDetailView, CategoryUpdateView

urlpatterns = [
    path('create-category/', CategoryCreateView.as_view(), name='create category'),
    path('update-category/<int:pk>/', CategoryUpdateView.as_view(), name='update category'),
    path('delete-category/<int:pk>/', delete_category, name='delete category'),
    path('create-product/', ProductCreateView.as_view(), name='create product'),
    path('update-product/<int:pk>/', update_product, name='update product'),
    path('delete-product/<int:pk>/', delete_product, name='delete product'),
    path('list-category/<int:pk>', CategoryDetailView.as_view(), name='list category'),
]
