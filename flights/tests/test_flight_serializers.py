from datetime import timedelta

import pytest
from django.utils import timezone

from flights.serializers import FlightWriteSerializer


@pytest.mark.django_db
def test_flight_write_serializer_valid_data(route, airplane, crew):
    flight_serializer = FlightWriteSerializer(data={
        "crew": [crew.id],
        "route": route.id,
        "airplane": airplane.id,
        "departure_time": timezone.now(),
        "arrival_time": timezone.now() + timedelta(hours=2),
    })
    assert flight_serializer.is_valid(), flight_serializer.errors

@pytest.mark.django_db
def test_flight_write_serializer_crew_cant_be_empty(route, airplane):
    flight_serializer = FlightWriteSerializer(data={
        "route": route.id,
        "airplane": airplane.id,
        "crew": [],
        "departure_time": timezone.now(),
        "arrival_time": timezone.now() + timedelta(hours=2),
    })
    assert not flight_serializer.is_valid()
    assert "crew" in flight_serializer.errors

@pytest.mark.django_db
def test_flight_write_serializer_arrival_before_departure_invalid(crew, route, airplane):
    serializer = FlightWriteSerializer(data={
        "route": route.id,
        "airplane": airplane.id,
        "crew": [crew.id],
        "departure_time": timezone.now(),
        "arrival_time": timezone.now() - timedelta(hours=1),
    })

    assert not serializer.is_valid()
    assert "Arrival time must be later" in str(serializer.errors)
