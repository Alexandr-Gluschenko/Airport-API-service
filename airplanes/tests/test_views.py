import pytest

from airplanes.models import Airplane


@pytest.mark.django_db
def test_airplane_admin_can_create(api_client, admin_user, airplane_type):

    api_client.force_authenticate(user=admin_user)

    payload = {
        "name": "Boeing 737",
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": airplane_type.id,
    }
    response = api_client.post('/api/airplanes/', payload)

    assert response.status_code == 201

    assert Airplane.objects.filter(name="Boeing 737").exists()

@pytest.mark.django_db
def test_airplane_user_cant_create(api_client, airplane_type):
    payload = {
        "name": "Boeing 737",
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": airplane_type.id,
    }
    response = api_client.post('/api/airplanes/', payload)

    assert response.status_code == 401

    assert not Airplane.objects.filter(name="Boeing 737").exists()

@pytest.mark.django_db
def test_airplane_auth_user_cant_create(api_client, user, airplane_type):
    api_client.force_authenticate(user=user)
    payload = {
        "name": "Boeing 737",
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": airplane_type.id,
    }
    response = api_client.post('/api/airplanes/', payload)

    assert response.status_code == 403
    assert not Airplane.objects.filter(name="Boeing 737").exists()

@pytest.mark.django_db
def test_airplane_auth_user_can_read(api_client, user, airplane_type):
    Airplane.objects.create(
        name="Boeing 737",
        rows=30,
        seats_in_rows=6,
        airplane_type=airplane_type,
    )
    api_client.force_authenticate(user=user)
    response = api_client.get('/api/airplanes/')

    assert response.status_code == 200
    assert response.data

