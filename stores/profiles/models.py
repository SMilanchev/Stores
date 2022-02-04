from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from stores.store.validators import capital_first_letter

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            capital_first_letter,
        ]
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            capital_first_letter,
        ]
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='profiles',
        blank=True
    )
    is_complete = models.BooleanField(
        default=False,
    )
    budget = models.FloatField(
        validators=[
            MinValueValidator(0),
        ]
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )