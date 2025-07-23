from django.db import models
from django.contrib.auth.models import User # Only import User once

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') # Added related_name for clarity
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    summary = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    # --- NEW CODE: Meta class with custom permissions ---
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    # --- END NEW CODE ---

class Library(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300, null=True, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

# --- RE-ADDED CODE: Librarian Model (for checker) ---
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField('Library', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# --- Your UserProfile Model (removed duplicate) ---
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"