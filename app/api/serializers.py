from rest_framework import serializers

from .helpers.serialization_errors import error_dict


class WeatherSerializer(serializers.Serializer):
    """Weather data serializer Class"""
    city = serializers.CharField(
        max_length=50,
        required=True,
        allow_null=False,
        error_messages={
            'required': error_dict['required'].format('city'),
        })
    days = serializers.IntegerField(
        min_value=1,
        max_value=10,
        required=True,
        allow_null=False,
        error_messages={
            'required': error_dict['required'].format('number of days'),
        })

    maximum = serializers.FloatField(read_only=True)
    minimum = serializers.FloatField(read_only=True)
    average = serializers.FloatField(read_only=True)
    median = serializers.FloatField(read_only=True)
