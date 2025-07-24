from bookshelf.models import Book
book = Book.objects.get(title="1984") # Or use book = Book.objects.first() if it's the only one
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")