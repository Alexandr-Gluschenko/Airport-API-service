import pytest

from airports.models import Airport
from routes.models import Route
from routes.serializers import RouteSerializer


@pytest.mark.django_db
def test_route_serializer_valid_data():
    airport_a = Airport.objects.create(name="Kyiv")
    airport_b = Airport.objects.create(name="Lviv")
    route = Route.objects.create(
        source=airport_a,
        destination=airport_b,
        distance=350,
    )
    serializer = RouteSerializer(route)

    data = serializer.data

    assert "id" in data
    assert "source" in data
    assert "destination" in data
    assert "distance" in data
    assert data["distance"] == route.distance

@pytest.mark.django_db
def test_route_serializer_missing_source(airport):
    serializer = RouteSerializer(data={
        "destination": airport.id,
        "distance": 200,
    })
    assert serializer.is_valid() == False
    assert "source" in serializer.errors

@pytest.mark.django_db
def test_route_serializer_invalid_destination_id(airport):
    serializer = RouteSerializer(data={
        "destination": 9999,
        "distance": 200,
        "source": airport.id,
    })
    assert serializer.is_valid() == False
    assert "destination" in serializer.errors