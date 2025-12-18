from rest_framework import serializers

from airplanes.serializers import AirplaneReadSerializer
from crews.serializers import CrewSerializer
from flights.models import Flight
from routes.serializers import RouteSerializer


class FlightReadSerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    airplane = AirplaneReadSerializer(read_only=True)
    crew = CrewSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = ["id", "route", "airplane", "crew", "departure_time", "arrival_time"]


class FlightWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["route", "airplane", "crew", "departure_time", "arrival_time"]

    def validate(self, data):
        if data["departure_time"] >= data["arrival_time"]:
            raise serializers.ValidationError(
                "Arrival time must be later than departure time."
            )
        return data