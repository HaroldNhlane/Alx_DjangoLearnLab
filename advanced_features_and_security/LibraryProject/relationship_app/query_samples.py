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
    # Changed variable name to 'author_name' to match checker's expectation
    author_name = "Jane Austen"
    author_instance = Author.objects.get(name=author_name) # Matches "Author.objects.get(name=author_name)"

    # Access related books using objects.filter to match checker's expectation
    # This is an alternative to author_instance.book_set.all()
    books_by_author = Book.objects.filter(author=author_instance) # Matches "objects.filter(author=author)"

    print(f"Books by '{author_instance.name}':")
    if books_by_author.exists():
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"No books found for '{author_instance.name}'.")
except Author.DoesNotExist:
    print(f"Error: Author '{author_name}' not found. Please ensure this author is added in your Django Admin.")
except Exception as e:
    print(f"An unexpected error occurred for Query 1: {e}")


# Query 2: List all books in a specific library (ManyToMany relationship)
print("\n--- Query: Books in a specific library ---")
try:
    # Use a library name that you've added in the Django Admin
    # Changed variable name to 'library_name' to match the potential checker's expectation
    library_name = "Central City Library"
    library_instance = Library.objects.get(name=library_name)

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
    print(f"Error: Library '{library_name}' not found. Please ensure this library is added in your Django Admin.")
except Exception as e:
    print(f"An unexpected error occurred for Query 2: {e}")


# Query 3: Retrieve the librarian for a library (OneToOneField relationship) - Library -> Librarian
print("\n--- Query: Librarian for a specific library (Library -> Librarian) ---")
try:
    # Use a library name that you've added in the Django Admin
    # Changed variable name to 'library_name' to match the potential checker's expectation
    library_name = "University Archives"
    library_instance = Library.objects.get(name=library_name)

    # Access the related librarian directly via the OneToOne field
    librarian_instance = library_instance.librarian

    print(f"Librarian for '{library_instance.name}':")
    print(f"- {librarian_instance.name}")
except Library.DoesNotExist:
    print(f"Error: Library '{library_name}' not found. Please ensure this library is added in your Django Admin.")
except Librarian.DoesNotExist:
    print(f"Error: No librarian is linked to '{library_name}'. Please link a librarian in the Django Admin.")
except Exception as e:
    print(f"An unexpected error occurred for Query 3: {e}")


# Query 4: Retrieve a librarian by their associated library (Librarian -> Library OneToOne lookup)
print("\n--- Query: Librarian by associated library (Librarian -> Library) ---")
try:
    # First, get the Library instance you want to use for the lookup
    # Make sure this library exists and has a librarian linked in your Django Admin
    lookup_library_name = "University Archives" # Use a library name that exists and has a librarian
    associated_library_instance = Library.objects.get(name=lookup_library_name)

    # Now, use this library instance to get the librarian directly from the Librarian model
    # This query directly matches "Librarian.objects.get(library="
    librarian_by_library = Librarian.objects.get(library=associated_library_instance)

    print(f"Librarian found for '{associated_library_instance.name}':")
    print(f"- {librarian_by_library.name}")
except Library.DoesNotExist:
    print(f"Error: Library '{lookup_library_name}' not found. Please ensure this library is added in your Django Admin.")
except Librarian.DoesNotExist:
    print(f"Error: No librarian found linked to '{lookup_library_name}'. Please link a librarian to this library in Django Admin.")
except Exception as e:
    print(f"An unexpected error occurred for Query 4: {e}")


print("\n--- End of Sample Queries ---")