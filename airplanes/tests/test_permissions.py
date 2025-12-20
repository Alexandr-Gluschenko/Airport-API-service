import pytest


@pytest.mark.django_db
def test_airplane_list_for_user_auth(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/airplanes/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_airplane_list_requires_auth(api_client):
    response = api_client.get("/api/airplanes/")
    assert response.status_code == 401


@pytest.mark.django_db
def test_airplane_create_forbidden_for_user(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post("/api/airplanes/", {})
    assert response.status_code == 403


@pytest.mark.django_db
def test_airplane_create_allowed_for_admin(api_client,
                                           admin_user, airplane_type):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post("/api/airplanes/", {
        "name": "Boeing 737",
        "rows": 30,
        "seats_in_rows": 6,
        "airplane_type": airplane_type.id,
    })

    assert response.status_code == 201


@pytest.mark.django_db
def test_airplane_update_forbidden_for_user(api_client, user, airplane):
    api_client.force_authenticate(user=user)
    response = api_client.patch(f'/api/airplanes/{airplane.id}/', {"rows": 40})
    assert response.status_code == 403


@pytest.mark.django_db
def test_airplane_delete_authenticated_user_forbidden(api_client,
                                                      user, airplane):
    api_client.force_authenticate(user=user)
    response = api_client.delete(f'/api/airplanes/{airplane.id}/')
    assert response.status_code == 403


@pytest.mark.django_db
def test_airplane_delete_unauthenticated(api_client, airplane):
    response = api_client.delete(f'/api/airplanes/{airplane.id}/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_airplane_delete_admin_allowed(api_client, admin_user, airplane):
    api_client.force_authenticate(user=admin_user)
    response = api_client.delete(f'/api/airplanes/{airplane.id}/')
    assert response.status_code == 204
