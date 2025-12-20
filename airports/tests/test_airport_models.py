import pytest

from airports.models import Airport


@pytest.mark.django_db
def test_airport_str():
    airport = Airport(name="Kyiv")
    assert str(airport) == airport.name
