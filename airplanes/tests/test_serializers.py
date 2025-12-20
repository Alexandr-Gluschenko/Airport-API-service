import pytest
from airplanes.models import AirPlaneType
from airplanes.serializers import AirplaneSerializer


@pytest.mark.django_db
def test_airplane_serializer_valid_data():
    airplane_type = AirPlaneType.objects.create(name="Boeing 737")

    serializer = AirplaneSerializer(data={
        "name": "Boeing 737",
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": airplane_type.id,
    })
    assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
def test_airplane_serializer_not_valid_data():
    serializer = AirplaneSerializer(data={
        "name": "Boeing 737",
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": 999,
    })
    assert not serializer.is_valid()
    assert "airplane_type" in serializer.errors


@pytest.mark.django_db
def test_airplane_serializer_name_cannot_be_blank():
    airplane_type = AirPlaneType.objects.create(name="Boeing 737")
    serializer = AirplaneSerializer(data={
        "name": "",
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": airplane_type.id,
    })
    assert not serializer.is_valid()
    assert "name" in serializer.errors


@pytest.mark.django_db
def test_airplane_serializer_name_is_required():
    airplane_type = AirPlaneType.objects.create(name="Boeing 737")
    serializer = AirplaneSerializer(data={
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": airplane_type.id,
    })
    assert not serializer.is_valid()
    assert "name" in serializer.errors
