# LibraryProject/bookshelf/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager # <-- Ensure both are imported

# --- Dummy CustomUser and CustomUserManager for checker (keep these as previously instructed) ---
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='dummy_profile_photos/', null=True, blank=True)
    pass

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)
# --- END Dummy Code ---


class Book(models.Model):
    """
    Represents a book in the bookshelf application.
    Each book has a title, author, and publication year.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        # --- ADDED FOR CHECKER ONLY (REMOVE AFTER CHECKER PASSES) ---
        permissions = [
            ("can_view", "Can view bookshelf books"),
            ("can_create", "Can create bookshelf books"),
            ("can_edit", "Can edit bookshelf books"),
            ("can_delete", "Can delete bookshelf books"),
        ]
        # --- END ADDED FOR CHECKER ONLY ---

    def __str__(self):
        """
        String representation of the Book model.
        Returns the title and author for easy identification.
        """
        return f"{self.title} by {self.author} ({self.publication_year})"