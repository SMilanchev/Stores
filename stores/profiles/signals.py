from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from stores.profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def profile_is_created(sender, instance, created, **kwargs):
    if created:
        if not instance.is_superuser:
            profile = Profile(user=instance)
            profile.save()