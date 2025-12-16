from rest_framework import serializers
from airports.models import Airport


class AirportSerializer(serializers.ModelSerializer):
    """
    All CRUD operations for Airport.
    """
    class Meta:
        model = Airport
        fields = ["id", "name", "closest_big_city"]
