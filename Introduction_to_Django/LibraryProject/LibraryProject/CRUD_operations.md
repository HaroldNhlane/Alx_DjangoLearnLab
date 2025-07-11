# Start the Django shell: python manage.py shell

# --- CREATE Operation ---
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected Output: 1984 by George Orwell (1949)

# --- RETRIEVE Operation ---
# Assuming the book created above is the first or only one, or retrieve by title
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")
# Expected Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
# ID: 1 (or another ID if other books exist)

# --- UPDATE Operation ---
book = Book.objects.get(title="1984") # Retrieve the book again
book.title = "Nineteen Eighty-Four"
book.save()
print(book)
# Expected Output: Nineteen Eighty-Four by George Orwell (1949)

# --- DELETE Operation ---
book = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve by the updated title
book.delete()
print("Book deleted.")
print(Book.objects.all()) # Confirm deletion
# Expected Output:
# Book deleted.
# <QuerySet []>

# Exit the Django shell: exit()