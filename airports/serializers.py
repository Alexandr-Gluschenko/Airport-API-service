import re

from rest_framework import serializers
from airports.models import Airport


class AirportSerializer(serializers.ModelSerializer):
    """
    All CRUD operations for Airport.
    """
    class Meta:
        model = Airport
        fields = ["id", "name", "closest_big_city"]

    def validate_name(self, value):
        if not re.match(r"^[A-Za-z\s-]+$", value):
            raise serializers.ValidationError("Name must contain only letters")
        return value

    def validate_closest_big_city(self, value):
        if not re.match(r"^[A-Za-z\s-]+$", value):
            raise serializers.ValidationError("Closest city"
                                              " must contain only letters")
        return value
