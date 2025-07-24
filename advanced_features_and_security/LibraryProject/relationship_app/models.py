# LibraryProject/relationship_app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager # <-- IMPORTANT: Import BaseUserManager
from django.conf import settings

# --- CustomUserManager (Step 3) ---
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


# --- CustomUser Model (UPDATED to use CustomUserManager) ---
class CustomUser(AbstractUser):
    """
    A custom user model extending Django's AbstractUser.
    Includes additional fields for date_of_birth and profile_photo.
    """
    # Important: Since we're making email the unique identifier,
    # you might want to consider making username optional or removing it
    # depending on your authentication strategy. For now, we'll keep it,
    # but the manager above focuses on email.
    email = models.EmailField(unique=True) # Ensure email is unique for login
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager() # <-- IMPORTANT: Tell CustomUser to use your custom manager

    USERNAME_FIELD = 'email' # <-- IMPORTANT: Define what field is used as username for login
    REQUIRED_FIELDS = ['username'] # Add other required fields if you have them (e.g., date_of_birth if mandatory)

    def __str__(self):
        return self.email # Or self.username if you prefer

# --- Your existing models ---

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    summary = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, null=True, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField('Library', on_delete=models.SET_NULL, null=True, blank=True)
    # If a Librarian is meant to *be* a CustomUser, or related:
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

# --- UserProfile Model: UPDATED to reference settings.AUTH_USER_MODEL ---
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='userprofile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"