from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(signal=post_save, sender=User)
def add_edit_user_prof(sender, instance: User, created: bool, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
    instance.details.save()
