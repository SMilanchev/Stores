from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

from stores.common.models import Product
from stores.profiles.models import Profile

UserModel = get_user_model()


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    is_send = models.BooleanField(
        default=False,
    )
    send_time = models.DateTimeField(
        auto_now=True,
    )


class OrderProducts(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    def clean_product(self):
        profile = Profile.objects.get(pk=self.order.user_id)
        if profile.budget - self.product.price < 0:
            raise ValidationError('Your budget is not enough to add this product!')
        else:
            profile.budget -= self.product.price
            profile.save(update_fields=['budget'])