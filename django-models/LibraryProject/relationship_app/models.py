from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Added null=True, blank=True for consistency and potential existing data
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # Added null=True, blank=True for consistency and potential existing data
    published_date = models.DateField(null=True, blank=True)
    # Added null=True, blank=True for consistency and potential existing data
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    # Added null=True, blank=True for consistency and potential existing data
    summary = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200) # Max length increased as per previous instruction
    # Added null=True, blank=True for consistency and potential existing data
    address = models.CharField(max_length=300, null=True, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
    # LibraryProject/relationship_app/models.py

from django.db import models
from django.contrib.auth.models import User

# ... (Your existing Author, Book, Library models) ...

# --- NEW/RE-ADDED CODE: Librarian Model (for checker) ---
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # This links a Librarian to a Library. Add null=True, blank=True for flexibility.
    library = models.OneToOneField('Library', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

# --- Your existing UserProfile Model ---
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

# --- NEW CODE: UserProfile Model ---
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