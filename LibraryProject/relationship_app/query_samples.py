# relationship_app/query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings') # Replace 'your_project_name'
django.setup()

# Now you can import your models
from relationship_app.models import Author, Book, Library, Librarian

print("--- Sample Queries ---")

# --- Query all books by a specific author (ForeignKey) ---
# Hint: You'll need to create some sample data first, either through the Django admin
# or by creating instances in this script like:
# Author.objects.create(name="Jane Doe")
# Book.objects.create(title="The First Book", author=Author.objects.get(name="Jane Doe"))
# etc.

# Example: Get an author and then get their books
# try:
#     author_jane = Author.objects.get(name="Jane Doe")
#     print(f"\nBooks by {author_jane.name}:")
#     for book in author_jane.book_set.all(): # 'book_set' is the reverse relationship name
#         print(f"- {book.title}")
# except Author.DoesNotExist:
#     print("\nAuthor 'Jane Doe' not found. Please create some sample data first.")


# --- List all books in a library (ManyToMany) ---
# Hint: Similar to above, make sure you have Library and Book instances linked.

# Example: Get a library and list its books
# try:
#     library_city = Library.objects.get(name="City Public Library")
#     print(f"\nBooks in {library_city.name}:")
#     for book in library_city.books.all():
#         print(f"- {book.title}")
# except Library.DoesNotExist:
#     print("\nLibrary 'City Public Library' not found. Please create sample data.")


# --- Retrieve the librarian for a library (OneToOneField) ---
# Hint: You'll need a Library and a linked Librarian instance.

# Example: Get a library and find its librarian
# try:
#     library_university = Library.objects.get(name="University Library")
#     print(f"\nLibrarian for {library_university.name}:")
#     print(f"- {library_university.librarian.name}")
# except Library.DoesNotExist:
#     print("\nLibrary 'University Library' not found. Please create sample data.")
# except Librarian.DoesNotExist: # This might happen if a library exists but no librarian is linked
#     print(f"No librarian found for {library_university.name}.")

print("\n--- End of Sample Queries ---")