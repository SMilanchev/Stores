from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from stores.stores_auth.managers import StoresUserManager


class StoresUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    USERNAME_FIELD = 'email'
    objects = StoresUserManager()