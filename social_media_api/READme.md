# Install Django and Django REST Framework
pip install django djangorestframework

# Create a new Django project
django-admin startproject social_media_api
cd social_media_api

# Create a new app for user accounts
python manage.py startapp accounts


# Add 'rest_framework', 'rest_framework.authtoken', and 'accounts' to INSTALLED_APPS

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',

    # Your apps
    'accounts',
]

Configure User Authentication
Next, we'll create a custom user model to include extra profile information. We'll also define the serializers for handling user registration and login data, and the views to process these requests.

Note: After creating the custom user model, you must update settings.py before running your first migration.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username

# Add this line to your settings.py to specify the custom user model
AUTH_USER_MODEL = 'accounts.CustomUser'

Define URL Patterns
Now, we'll set up the API endpoints. We create URL patterns for our `accounts` app and include them in the main project's URL configuration. This makes our registration and login endpoints accessible.

Testing and Initial Launch
Finally, apply the database migrations to create your new user model table and run the development server. You can then use a tool like Postman to test the /api/accounts/register/ and /api/accounts/login/ endpoints.


# Create and apply database migrations
python manage.py makemigrations accounts
python manage.py migrate

# Start the development server
python manage.py runserver


pip install Pillow

What is Pillow?
Pillow is a powerful library for image processing in Python. Django's ImageField relies on it to handle image-related tasks such as validating file formats, getting image dimensions, and resizing images. Without Pillow, Django is unable to process the images you intend to upload for user profiles.