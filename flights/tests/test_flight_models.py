import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from flights.models import Flight


@pytest.mark.django_db
def test_flight_arrival_time_must_be_after_departure_time(route, airplane):
    departure = timezone.now()
    arrival = departure - timedelta(hours=1)

    flight = Flight(
        route=route,
        airplane=airplane,
        departure_time=departure,
        arrival_time=arrival,
    )

    with pytest.raises(ValidationError) as info:
        flight.full_clean()

    assert "arrival_time" in info.value.message_dict


@pytest.mark.django_db
def test_flight_with_valid_times_is_valid(route, airplane):
    departure = timezone.now()
    arrival = departure + timedelta(hours=2)
    flight = Flight(
        route=route,
        airplane=airplane,
        departure_time=departure,
        arrival_time=arrival,
    )

    flight.full_clean()


@pytest.mark.django_db
def test_flight_arrival_equal_departure_is_invalid(route, airplane):
    time = timezone.now()
    flight = Flight(
        route=route,
        airplane=airplane,
        departure_time=time,
        arrival_time=time,
    )
    with pytest.raises(ValidationError):
        flight.full_clean()
