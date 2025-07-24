# LibraryProject/relationship_app/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # For CustomUserAdmin
from .models import Author, Book, Library, Librarian, UserProfile, CustomUser # Import CustomUser

# --- NEW: CustomUserAdmin (Step 4) ---
class CustomUserAdmin(UserAdmin):
    """
    Custom Admin class for CustomUser model.
    Adds date_of_birth and profile_photo to the admin interface.
    """
    # Define the fields to be displayed in the list view
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo',)

    # Define the fields to be edited in the form view
    fieldsets = UserAdmin.fieldsets + (
        (('Custom Fields'), {'fields': ('date_of_birth', 'profile_photo',)}),
    )
    # If you have 'add_fieldsets' for user creation, you might need to extend that too:
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('Custom Fields'), {'fields': ('date_of_birth', 'profile_photo',)}),
    )

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)

# --- Register CustomUser with your CustomUserAdmin (Step 4) ---
admin.site.register(CustomUser, CustomUserAdmin)