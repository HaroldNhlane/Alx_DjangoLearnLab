# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class BookListViewTest(APITestCase):
    def test_list_books(self):
        """
        Ensure we can retrieve a list of books.
        """
        # Get the URL for the BookListView
        url = reverse('book-list')
        
        # Simulate a GET request to that URL
        response = self.client.get(url)
        
        # Check that the status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that the response data is an empty list, as no books exist yet
        self.assertEqual(response.data, [])