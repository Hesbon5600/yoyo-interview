import requests
from django.conf import settings
from rest_framework.serializers import ValidationError


def compute_temperature_stats(city, days):
    """
    Compute the minimum, maximum, average, and median temperature
    Args:
        city:(str) the city to compute the stats for
        days:(int) the number of days to compute the stats for
    Returns:
        data: (dict) the stats for the city
    """
    # Get the weather data from the weatherapi
    url = f"https://api.weatherapi.com/v1/forecast.json?key={settings.WEATHER_API_KEY}&q={city}&days={days}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        raise ValidationError(data["error"]["message"])
    temperatures = []
    raw_data = data.get('forecast', {}).get('forecastday', [])
    for day in raw_data:
        for hour in day.get('hour', []):
            temperatures.append(hour.get('temp_c'))
    # Compute the stats
    data = {
        "maximum": round(max(temperatures), 2),
        "minimum": round(min(temperatures), 2),
        "average": round(sum(temperatures) / len(temperatures), 2),
        "median": round(sorted(temperatures)[len(temperatures) // 2], 2),
    }
    return data
