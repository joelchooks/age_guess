from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class HumanAgeViewIntegrationTestCase(TestCase):
    """Integration test cases for HumanAgeView API."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    def test_human_age_view_integration(self):
        """Test HumanAgeView API with valid request."""
        url = reverse('human_age_view')
        data = {'name': 'Michael'}
        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('name', response.data)
        self.assertIn('age', response.data)
        self.assertIn('date_of_birth', response.data)

    def test_human_age_view_integration_invalid_request(self):
        """Test HumanAgeView API with invalid request."""
        url = reverse('human_age_view')
        data = {}  # Invalid request data
        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


