import pytest


@pytest.mark.django_db
def test_flight_list_returns_401(api_client):
    response = api_client.get('/api/flights/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_admin_can_update_flight(api_client, admin_user, flight):
    api_client.force_authenticate(user=admin_user)
    response = api_client.patch(
        f"/api/flights/{flight.id}/",
        {
            "departure_time": "2025-12-18T20:00:00Z",
            "arrival_time": "2025-12-18T22:00:00Z",
         },
        format="json",
    )

    assert response.status_code == 200
    assert response.data["arrival_time"] == "2025-12-18T22:00:00Z"
