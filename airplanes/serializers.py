from rest_framework import serializers
from airplanes.models import Airplane, AirPlaneType


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ["name", "rows", "seats_in_rows", "airplane_type"]

class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirPlaneType
        fields = ["id", "name"]


class AirplaneWriteSerializer(serializers.ModelSerializer):
    """
    Used for create and update operations.
    """
    class Meta:
        model = Airplane
        fields = ["name", "rows", "seats_in_rows", "airplane_type"]


class AirplaneReadSerializer(serializers.ModelSerializer):
    airplane_type = AirplaneTypeSerializer(read_only=True)
    class Meta:
        model = Airplane
        fields = ["id", "name", "rows", "seats_in_rows", "airplane_type"]
