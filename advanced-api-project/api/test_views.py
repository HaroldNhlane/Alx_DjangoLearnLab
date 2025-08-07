# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from api.models import Book

class BookListViewTest(APITestCase):
    def test_list_books_no_data(self):
        """
        Ensure the list view returns an empty list when no books exist.
        """
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

class BookCreateViewTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Get the URL for the BookCreateView
        self.url = reverse('book-create')
        
        # Sample data for a new book
        self.valid_data = {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'}
    
    def test_create_book_authenticated_user(self):
        """
        Ensure an authenticated user can create a new book.
        """
        # Log in the user
        self.client.login(username='testuser', password='password123')
        
        # Make a POST request with the test data
        response = self.client.post(self.url, self.valid_data, format='json')
        
        # Assert that the request was successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Assert that the book was added to the database
        self.assertEqual(Book.objects.count(), 1)
        
    def test_create_book_unauthenticated_user(self):
        """
        Ensure an unauthenticated user cannot create a book.
        """
        # Do not log in the user
        response = self.client.post(self.url, self.valid_data, format='json')
        
        # Assert that the request was forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Assert that no book was added to the database
        self.assertEqual(Book.objects.count(), 0)