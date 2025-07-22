# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters to the sidebar
    list_filter = ('publication_year', 'author') # Assuming 'author' is a ForeignKey or simple field

    # Enable search across these fields
    search_fields = ('title', 'author__name') # Use 'author' if it's a CharField directly on Book, else 'author__name' for ForeignKey
    # If your Author model has fields like 'first_name', 'last_name', you could do ('title', 'author__first_name', 'author__last_name')

admin.site.register(Book, BookAdmin
                    )
