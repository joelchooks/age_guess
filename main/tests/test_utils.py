from django.test import TestCase
from django.core.cache import cache
from unittest.mock import patch
from ..models import get_cached_request_response
from ..utils import fetch_age_from_agify



class UtilsTestCase(TestCase):
    """Test cases for utility functions in main.utils."""

    @patch('main.utils.requests.get')
    def test_fetch_age_from_agify_success(self, mock_get):
        """Test fetching age from Agify API with successful response."""
        mock_response = {'age': 25}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        age, date_of_birth = fetch_age_from_agify('Michael')
        self.assertEqual(age, 25)
        self.assertIsInstance(date_of_birth, int)

    @patch('main.utils.requests.get')
    def test_fetch_age_from_agify_invalid_response(self, mock_get):
        """Test fetching age from Agify API with invalid response."""
        mock_get.return_value.status_code = 404

        age, date_of_birth = fetch_age_from_agify('Michael')
        self.assertIsNone(age)
        self.assertIsNone(date_of_birth)


class ModelsTestCase(TestCase):
    """Test cases for models in main."""

    def test_get_cached_request_response_cached(self):
        """Test retrieving cached response."""
        # Mock cached response
        cached_response = {'name': 'Michael', 'age': 30, 'date_of_birth': 1992}
        cache.set('Michael', cached_response)

        # Call the function
        response = get_cached_request_response('Michael')

        # Assert cached response is returned
        self.assertEqual(response, cached_response)

    def test_get_cached_request_response_not_cached(self):
        """Test fetching data and caching response."""
        # Mock the fetch_age_from_agify function
        with patch('main.models.fetch_age_from_agify') as mock_fetch_age_from_agify:
            # Mock response from fetch_age_from_agify
            mock_fetch_age_from_agify.return_value = (30, 1992)

            # Call the function
            response = get_cached_request_response('Michael')

            # Assert response is correct
            self.assertEqual(response, {'name': 'Michael', 'age': 30, 'date_of_birth': 1992})

