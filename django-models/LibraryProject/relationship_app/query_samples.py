# relationship_app/query_samples.py

import os
import django

# Set up Django environment
# IMPORTANT: Replace 'your_project_name' with the actual name of your project's main directory
# For example, if your project folder is 'LibraryProject', it should be 'LibraryProject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Now import your models
from relationship_app.models import Author, Book, Library, Librarian

print("--- Sample Queries ---")

# --- IMPORTANT: Ensure you have sample data in your database first! ---
# You can add data via the Django Admin (http://127.0.0.1:8000/admin/)
# or by uncommenting and running the data creation below once, then re-commenting.

# Example data creation (uncomment, run once, then re-comment or remove)
# try:
#     author1, created = Author.objects.get_or_create(name="Jane Austen")
#     author2, created = Author.objects.get_or_create(name="J.R.R. Tolkien")
#     author3, created = Author.objects.get_or_create(name="Harper Lee")

#     book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
#     book2, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)
#     book3, created = Book.objects.get_or_create(title="The Hobbit", author=author2)
#     book4, created = Book.objects.get_or_create(title="To Kill a Mockingbird", author=author3)

#     library1, created = Library.objects.get_or_create(name="Central City Library")
#     library2, created = Library.objects.get_or_create(name="University Archives")

#     if created: # Only add books to libraries if they were just created to avoid duplicates on re-run
#         library1.books.add(book1, book2, book3)
#         library2.books.add(book3, book4)

#     librarian1, created = Librarian.objects.get_or_create(name="Alice Librarian", library=library1)
#     librarian2, created = Librarian.objects.get_or_create(name="Bob Bookshelf", library=library2)

#     print("\nSample data ensured/created.")
# except Exception as e:
#     print(f"\nError creating sample data: {e}. Please ensure migrations are applied and models are correct.")


# --- Query 1: Query all books by a specific author (ForeignKey relationship) ---
# Let's try to get books by 'Jane Austen' (or an author you've created)
print("\n--- Query: Books by a specific author ---")
try:
    target_author_name = "Jane Austen" # Change this to an author name you've added
    author = Author.objects.get(name=target_author_name)
    books_by_author = author.book_set.all() # Use the reverse relationship manager (lowercase model name + _set)

    print(f"Books by '{author.name}':")
    if books_by_author.exists():
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"No books found for '{author.name}'.")
except Author.DoesNotExist:
    print(f"Author '{target_author_name}' not found. Please add this author in the admin or ensure the name matches.")
except Exception as e:
    print(f"An error occurred: {e}")

# --- Query 2: List all books in a library (ManyToMany relationship) ---
# Let's try to get books from 'Central City Library' (or a library you've created)
print("\n--- Query: Books in a specific library ---")
try:
    target_library_name = "Central City Library" # Change this to a library name you've added
    library = Library.objects.get(name=target_library_name)
    books_in_library = library.books.all() # Access the ManyToMany related objects directly

    print(f"Books in '{library.name}':")
    if books_in_library.exists():
        for book in books_in_library:
            print(f"- {book.title} by {book.author.name}") # We can even get the author here!
    else:
        print(f"No books found in '{library.name}'.")
except Library.DoesNotExist:
    print(f"Library '{target_library_name}' not found. Please add this library in the admin or ensure the name matches.")
except Exception as e:
    print(f"An error occurred: {e}")

# --- Query 3: Retrieve the librarian for a library (OneToOneField relationship) ---
# Let's try to get the librarian for 'University Archives' (or a library you've created)
print("\n--- Query: Librarian for a specific library ---")
try:
    target_library_name = "University Archives" # Change this to a library name you've added
    library = Library.objects.get(name=target_library_name)
    librarian = library.librarian # Access the OneToOne related object directly

    print(f"Librarian for '{library.name}':")
    print(f"- {librarian.name}")
except Library.DoesNotExist:
    print(f"Library '{target_library_name}' not found. Please add this library in the admin or ensure the name matches.")
except Librarian.DoesNotExist: # This handles the case where a Library exists but no Librarian is linked via OneToOne
    print(f"No librarian found for '{target_library_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")


print("\n--- End of Sample Queries ---")