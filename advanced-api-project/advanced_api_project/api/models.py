from django.db import models

class Author(models.Model):
    """
    The Author model represents a book's author.
    It has a single field, `name`, to store the author's full name.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a single book.
    It includes the book's title, publication year, and a foreign key
    linking it to an Author, creating a one-to-many relationship
    where one author can have multiple books.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title