from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='profiles',
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )