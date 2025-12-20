import pytest
from django.db import IntegrityError
from airplanes.models import Airplane, AirPlaneType


@pytest.mark.django_db
def test_airplane_str():
    airplane_type = AirPlaneType.objects.create(name="Boeing 737")
    airplane = Airplane(name="Boeing 737",
                        rows=30,
                        seats_in_rows=6,
                        airplane_type=airplane_type)

    assert str(airplane) == airplane.name


@pytest.mark.django_db
def test_cant_create_airplane_with_same_name():
    airplane_type = AirPlaneType.objects.create(name="Passenger")

    Airplane.objects.create(
        name="Boeing 737",
        rows=30,
        seats_in_rows=6,
        airplane_type=airplane_type,
    )

    with pytest.raises(IntegrityError):
        Airplane.objects.create(
            name="Boeing 737",
            rows=25,
            seats_in_rows=3,
            airplane_type=airplane_type,
        )


@pytest.mark.django_db
def test_cant_create_airplane_without_airplane_type():
    with pytest.raises(IntegrityError):
        Airplane.objects.create(
            name="Boeing 737",
            rows=25,
            seats_in_rows=3,
            airplane_type=None,
        )


@pytest.mark.django_db
def test_on_unavailability_negative_rows_and_seats_airplane():
    airplane_type = AirPlaneType.objects.create(name="Passenger")
    with pytest.raises(IntegrityError):
        Airplane.objects.create(
            name="Boeing 737",
            rows=-25,
            seats_in_rows=-3,
            airplane_type=airplane_type,
        )


@pytest.mark.django_db
def test_airplane_cant_create_without_rows_and_seats():
    airplane_type = AirPlaneType.objects.create(name="Passenger")
    with pytest.raises(IntegrityError):
        Airplane.objects.create(
            name="Boeing 737",
            rows=None,
            seats_in_rows=None,
            airplane_type=airplane_type,
        )
