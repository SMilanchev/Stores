from django.contrib import admin

# Register your models here.
from stores.common.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass