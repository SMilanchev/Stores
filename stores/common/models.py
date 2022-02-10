from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(
        max_length=20,
        unique=True,
    )
    image = models.ImageField(
        upload_to='categories',
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=40,
    )
    image = models.ImageField(
        upload_to='products',
    )
    description = models.TextField(
        max_length=200,
    )
    category_type = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    price = models.FloatField(
        validators=[
            MinValueValidator(0),
        ]
    )