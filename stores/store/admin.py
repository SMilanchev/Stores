from django.contrib import admin

# Register your models here.
from stores.store.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass