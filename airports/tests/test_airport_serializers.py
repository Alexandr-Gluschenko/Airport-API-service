import pytest

from airports.serializers import AirportSerializer

@pytest.mark.django_db
def test_airport_serializer_valid_data():
    serializer = AirportSerializer(data={
        "name": "Kyiv",
        "closest_big_city": "Kyiv"
    })
    assert serializer.is_valid(), serializer.errors

@pytest.mark.django_db
def test_airport_serializer_not_valid_data():
    serializer = AirportSerializer(data={
        "name": "132",
        "closest_big_city": "222"
    })
    assert not serializer.is_valid(), serializer.errors

@pytest.mark.django_db
def test_airport_serializer_without_name():
    serializer = AirportSerializer(data={
        "closest_big_city": "Kyiv"
    })
    assert not serializer.is_valid(), serializer.errors