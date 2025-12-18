from rest_framework import status

from airports.models import Airport
from conftest import api_client
from airports.serializers import AirportSerializer
from airports.tests.base_api_test import BaseAirportAPITest


class AirportAPITest(BaseAirportAPITest):
    url = "/api/airports/"
    payload = {
        "name": "Heathrow",
        "closest_big_city": "London",
    }
