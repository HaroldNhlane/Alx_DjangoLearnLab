# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Book

class BookCreateViewTest(APITestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Get the URL for the CreateView
        self.url = reverse('book-create')
        
        # Data for a new book
        self.valid_data = {
            'title': 'Test Book', 
            'author': 'Test Author', 
            'publication_year': 2024
        }
    
    def test_create_book_authenticated(self):
        """
        Ensure we can create a new book as an authenticated user.
        """
        # Log in the user before making the request
        self.client.login(username='testuser', password='password123')
        
        # Make a POST request with valid data
        response = self.client.post(self.url, self.valid_data, format='json')
        
        # Check that the status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check that the book was created in the database
        self.assertEqual(Book.objects.count(), 1)
        
        # Check that the returned data is correct
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_create_book_unauthenticated(self):
        """
        Ensure an unauthenticated user cannot create a book.
        """
        # Do not log in the user
        response = self.client.post(self.url, self.valid_data, format='json')
        
        # Check that the status code is 403 Forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Check that no book was created in the database
        self.assertEqual(Book.objects.count(), 0)