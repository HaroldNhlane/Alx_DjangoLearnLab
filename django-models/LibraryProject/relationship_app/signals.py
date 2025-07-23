# LibraryProject/relationship_app/signals.py

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create or update a UserProfile whenever a User is saved.
    If 'created' is True (new user), a UserProfile is created.
    If 'created' is False (existing user), the profile is saved if it exists.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Optional: If you want to ensure the profile is always saved when the user is saved
    # instance.userprofile.save()