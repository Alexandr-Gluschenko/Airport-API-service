from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIClient

from airplanes.models import AirPlaneType, Airplane
from airports.models import Airport
from crews.models import Crew
from flights.models import Flight
from orders.models import Order
from routes.models import Route

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        username='test',
        email="test@test.com",
        password="password123"
    )


@pytest.fixture
def airplane_type(db):
    return AirPlaneType.objects.create(
        name="Boeing",
    )

@pytest.fixture
def airplane(db, airplane_type):
    return Airplane.objects.create(
        name="Boeing 737",
        rows=30,
        seats_in_rows=6,
        airplane_type=airplane_type,
    )

@pytest.fixture
def crew(db, airplane_type):
    return Crew.objects.create(
        first_name="Test",
        last_name="Test1",
    )

@pytest.fixture
def airport(db):
    return Airport.objects.create(
        name="Boryspil",
        closest_big_city="Kyiv"
    )

@pytest.fixture
def route(airport):
    destination = Airport.objects.create(
        name="Boryspil",
        closest_big_city="Kyiv",
    )

    return Route.objects.create(
        source=airport,
        destination=destination,
        distance=540,
    )

@pytest.fixture
def flight(route, airplane, crew):
    flight = Flight.objects.create(
        route=route,
        airplane=airplane,
        departure_time=timezone.now(),
        arrival_time=timezone.now() + timedelta(hours=2),
    )
    flight.crew.add(crew)
    return flight

@pytest.fixture
def order(user):
    return Order.objects.create(user=user)

@pytest.fixture
def another_user(django_user_model):
    return django_user_model.objects.create_user(
        username="another_user",
        password="password123"
    )
