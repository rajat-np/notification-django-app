from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from notifications.signals import notify

from notification_django_app.users.models import User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a notification when a user is created"""

    if created:
        notify.send(instance, recipient=instance, verb='Your account is created')
