# api/models.py

from django.db import models

# Model for representing an Author
class Author(models.Model):
    """
    The Author model stores information about a book's author.
    It has a one-to-many relationship with the Book model, meaning one author
    can be associated with multiple books.
    """
    name = models.CharField(max_length=100)  # The author's full name.

    def __str__(self):
        return self.name

# Model for representing a Book
class Book(models.Model):
    """
    The Book model stores information about a book, including its title,
    publication year, and a foreign key to its author.
    """
    title = models.CharField(max_length=200)  # The title of the book.
    publication_year = models.IntegerField() # The year the book was published.
    # The ForeignKey creates a one-to-many relationship. The `related_name`
    # 'books' allows us to access all books of an author using `author_instance.books.all()`.
    # `on_delete=models.CASCADE` ensures that if an Author is deleted,
    # all their books are also deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author.name}"