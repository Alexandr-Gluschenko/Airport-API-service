import pytest

from airports.models import Airport


@pytest.mark.django_db
def test_anonymous_cannot_retrieve_routes(api_client):
    response = api_client.get("/api/routes/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_authorized_user_can_read_route(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/routes/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_authorized_user_cant_create_routes(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post("/api/routes/")
    assert response.status_code == 403


@pytest.mark.django_db
def test_route_admin_can_create_routes(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)

    source = Airport.objects.create(name="Kyiv")
    destination = Airport.objects.create(name="Lviv")

    data = {
        "source": source.id,
        "destination": destination.id,
        "distance": 350,
    }

    response = api_client.post("/api/routes/", data)
    assert response.status_code == 201
