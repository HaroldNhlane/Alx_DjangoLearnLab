from django.db import models

class Book(models.Model):
    """
    Represents a book in the bookshelf application.
    Each book has a title, author, and publication year.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """
        String representation of the Book model.
        Returns the title and author for easy identification.
        """
        return f"{self.title} by {self.author} ({self.publication_year})"

