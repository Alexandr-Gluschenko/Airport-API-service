from airports.tests.base_api_test import BaseAirportAPITest


class AirportAPITest(BaseAirportAPITest):
    url = "/api/airports/"
    payload = {
        "name": "Heathrow",
        "closest_big_city": "London",
    }
