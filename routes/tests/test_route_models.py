import pytest
from django.core.exceptions import ValidationError

from airports.models import Airport
from routes.models import Route


@pytest.mark.django_db
def test_route_correctly_created_valid_data():
    airport_a = Airport.objects.create(name="Kyiv")
    airport_b = Airport.objects.create(name="Lviv")
    Route.objects.create(
        source=airport_a,
        destination=airport_b,
        distance=350,
    )
    assert Route.objects.count() == 1


@pytest.mark.django_db
def test_route_model_rejects_negative_distance():
    airport_a = Airport.objects.create(name="Kyiv")
    airport_b = Airport.objects.create(name="Lviv")
    route = Route(
        source=airport_a,
        destination=airport_b,
        distance=-20,
    )
    with pytest.raises(ValidationError):
        route.full_clean()


@pytest.mark.django_db
def test_correctly_operation_of_related_objects():
    airport_a = Airport.objects.create(name="Kyiv")
    airport_b = Airport.objects.create(name="Lviv")
    route = Route.objects.create(
        source=airport_a,
        destination=airport_b,
        distance=350,
    )
    assert airport_a.routes_from.count() == 1
    assert airport_b.routes_to.count() == 1
    assert route in airport_a.routes_from.all()


@pytest.mark.django_db
def test_route_deleted_when_source_airport_deleted():
    source = Airport.objects.create(name="Kyiv")
    destination = Airport.objects.create(name="Lviv")
    route = Route.objects.create(
        source=source,
        destination=destination,
        distance=350,
    )

    assert Route.objects.count() == 1

    route.delete()

    assert Route.objects.count() == 0


@pytest.mark.django_db
def test_route_deleted_when_destination_airport_deleted():
    source = Airport.objects.create(name="Kyiv")
    destination = Airport.objects.create(name="Lviv")
    route = Route.objects.create(
        source=source,
        destination=destination,
        distance=350,
    )

    route.delete()

    assert Route.objects.count() == 0
