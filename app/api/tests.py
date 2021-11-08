from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status


class TestWeatherStats(APITestCase):
    """
    Api test cases
    """

    def setUp(self):
        """
        Setup base test variables
        """
        self.base_url = reverse('weather-stats', kwargs={"city": "Nairobi"})
        self.days_query_params = {'days': 2}

    def test_fetch_city_weather_stats_successfully(self):
        """
        Fetch city weather stats successfully
        """
        response = self.client.get(self.base_url, self.days_query_params,
                                   format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(data, dict)
        self.assertIn('maximum', data)

    def test_fetch_city_weather_invalid_city_fails(self):
        """
        Fetch city weather stats with invalid city fails
        """
        response = self.client.get(reverse('weather-stats',
                                           kwargs={"city": "invalidcity"}),
                                   self.days_query_params,
                                   format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(data, dict)
        self.assertIn('No matching location found', data['errors'][0])

    def test_fetch_city_weather_invalid_days_fails(self):
        """
        Fetch city weather stats with invalid days fails
        """
        response = self.client.get(self.base_url, {"days": 100},
                                   format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(data, dict)
        self.assertIn('Ensure this value is less than or equal to 10',
                      data['errors']['days'][0])

    def test_fetch_city_weather_missing_fields_fails(self):
        """
        Fetch city weather stats with invalid days fails
        """
        response = self.client.get(self.base_url, format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(data, dict)
        self.assertIn('This field may not be null', data['errors']['days'][0])
