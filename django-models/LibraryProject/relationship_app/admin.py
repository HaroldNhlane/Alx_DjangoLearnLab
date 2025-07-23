# LibraryProject/relationship_app/admin.py

from django.contrib import admin
# --- CORRECTED LINE: Removed Librarian, Added UserProfile ---
from .models import Author, Book, Library, UserProfile

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
# --- NEW LINE: Register UserProfile for admin interface ---
admin.site.register(UserProfile)