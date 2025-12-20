from datetime import timedelta

import pytest
from django.utils import timezone

from flights.models import Flight


@pytest.mark.django_db
def test_flight_list_for_anonymous_user(api_client):
    response = api_client.get("/api/flights/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_flight_list_for_authenticated_user(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/flights/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_flight_create_for_admin(api_client,
                                 admin_user,
                                 crew,
                                 airplane,
                                 route):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post("/api/flights/", {
        "crew": [crew.id],
        "route": route.id,
        "airplane": airplane.id,
        "departure_time": "2025-12-18T20:00:00Z",
        "arrival_time": "2025-12-18T22:00:00Z",
    },
                               format="json",
                               )
    assert response.status_code == 201


@pytest.mark.django_db
def test_flight_create_for_authenticated_user_forbidden(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post("/api/flights/", {})
    assert response.status_code == 403


@pytest.mark.django_db
def test_flight_delete_for_admin(
    api_client,
    admin_user,
    route,
    airplane,
    crew,
):
    api_client.force_authenticate(user=admin_user)

    flight = Flight.objects.create(
        route=route,
        airplane=airplane,
        departure_time=timezone.now(),
        arrival_time=timezone.now() + timedelta(hours=2),
    )
    flight.crew.add(crew)
    response = api_client.delete(f"/api/flights/{flight.id}/")

    assert response.status_code == 204
    assert not Flight.objects.filter(id=flight.id).exists()
