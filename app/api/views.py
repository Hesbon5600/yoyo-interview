from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .helpers.weather_stats import compute_temperature_stats
from .serializers import WeatherSerializer


class WeatherStatsAPIView(generics.RetrieveAPIView):
    """Class to handle getting weather stats"""
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
    serializer_class = WeatherSerializer
    days_request_param = openapi.Parameter(
        'days', openapi.IN_QUERY,
        description="number of days to get weather stats",
        type=openapi.TYPE_INTEGER,
        required=True)

    @swagger_auto_schema(method='get',
                         manual_parameters=[days_request_param])
    @action(methods=['GET'], detail=True)
    def get(self, request, city):
        """
        override the get method to get weather stats
        Args:
            request: (obj) request object
            city: (str) city name
        Returns:
            (obj) response object containing the city weather stats
        """
        data = {'city': city, 'days': request.query_params.get('days', None)}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        stats = compute_temperature_stats(city, data.get('days'))
        return Response(stats, status=status.HTTP_200_OK)
