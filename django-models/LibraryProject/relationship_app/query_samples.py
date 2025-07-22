# relationship_app/query_samples.py

import os
import django

# Set up Django environment
# IMPORTANT: Replace 'your_project_name' with the actual name of your Django project's main directory
# For example, if your project folder is 'LibraryProject', it should be 'LibraryProject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Now import your models
from relationship_app.models import Author, Book, Library, Librarian

print("--- Starting Sample Queries ---")

# --- Reminder: Ensure you have sample data in your database first! ---
# Use the Django Admin (http://127.0.0.1:8000/admin/) to add authors, books, libraries, and librarians.
# Make sure the names below match the data you've entered.

# Query 1: Query all books by a specific author (ForeignKey relationship)
print("\n--- Query: Books by a specific author ---")
try:
    # Use an author name that you've added in the Django Admin
    target_author_name = "Jane Austen"
    author_instance = Author.objects.get(name=target_author_name)
    
    # Access related books using the reverse relationship manager (model_name_set)
    books_by_author = author_instance.book_set.all() 

    print(f"Books by '{author_instance.name}':")
    if books_by_author.exists():
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"No books found for '{author_instance.name}'.")
except Author.DoesNotExist:
    print(f"Error: Author '{target_author_name}' not found. Please ensure this author is added in your Django Admin.")
except Exception as e:
    print(f"An unexpected error occurred for Query 1: {e}")


# Query 2: List all books in a library (ManyToMany relationship)
print("\n--- Query: Books in a specific library ---")
try:
    # Use a library name that you've added in the Django Admin
    target_library_name = "Central City Library"
    library_instance = Library.objects.get(name=target_library_name)
    
    # Access related books directly via the ManyToMany field
    books_in_library = library_instance.books.all() 

    print(f"Books in '{library_instance.name}':")
    if books_in_library.exists():
        for book in books_in_library:
            # For each book, you can also access its author via the ForeignKey
            print(f"- {book.title} by {book.author.name}") 
    else:
        print(f"No books found in '{library_instance.name}'.")
except Library.DoesNotExist:
    print(f"Error: Library '{target_library_name}' not found. Please ensure this library is added in your Django Admin.")
except Exception as e:
    print(f"An unexpected error occurred for Query 2: {e}")


# Query 3: Retrieve the librarian for a library (OneToOneField relationship)
print("\n--- Query: Librarian for a specific library ---")
try:
    # Use a library name that you've added in the Django Admin
    target_library_name = "University Archives"
    library_instance = Library.objects.get(name=target_library_name)
    
    # Access the related librarian directly via the OneToOne field
    librarian_instance = library_instance.librarian 

    print(f"Librarian for '{library_instance.name}':")
    print(f"- {librarian_instance.name}")
except Library.DoesNotExist:
    print(f"Error: Library '{target_library_name}' not found. Please ensure this library is added in your Django Admin.")
except Librarian.DoesNotExist:
    print(f"Error: No librarian is linked to '{target_library_name}'. Please link a librarian in the Django Admin.")
except Exception as e:
    print(f"An unexpected error occurred for Query 3: {e}")

print("\n--- End of Sample Queries ---")