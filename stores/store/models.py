from django.contrib.auth import get_user_model
from django.db import models
from stores.common.models import Category
from stores.location.validators import check_coordinates_valid
from stores.store.validators import capital_first_letter, check_coordinates_numbers

UserModel = get_user_model()


class Store(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            capital_first_letter,
        ]
    )
    image = models.ImageField(
        upload_to='stores'
    )
    description = models.TextField(
        max_length=200,
    )
    location = models.CharField(
        max_length=80,
        validators=[
            check_coordinates_numbers,
            check_coordinates_valid,
        ]
    )
    categories = models.ManyToManyField(
        Category,
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
