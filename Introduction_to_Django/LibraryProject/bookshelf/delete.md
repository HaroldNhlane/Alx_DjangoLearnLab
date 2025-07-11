from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve by the updated title
book.delete()
print("Book deleted.")
print(Book.objects.all()) # Should show an empty QuerySet
