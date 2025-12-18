import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from airplanes.models import AirPlaneType, Airplane

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