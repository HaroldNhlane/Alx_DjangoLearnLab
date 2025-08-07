# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book # Don't forget this import!

class BookListViewTest(APITestCase):
    def test_list_books_no_data(self):
        """
        Ensure the list view returns an empty list when no books exist.
        """
        # Get the URL for the BookListView
        url = reverse('book-list')
        
        # Simulate a GET request to that URL
        response = self.client.get(url)
        
        # Check that the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that the response data is an empty list
        self.assertEqual(response.data, [])