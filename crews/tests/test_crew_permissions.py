VALID_PAYLOAD = {
    "first_name": "Albert",
    "last_name": "Krylov",
}


def test_crew_list_return_401_for_anonymous(api_client):
    response = api_client.get("/api/crews/")
    assert response.status_code == 401


def test_crew_list_return_200_for_authenticate_user(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/crews/")
    assert response.status_code == 200


def test_crew_create_return_403_for_authenticate_user(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post("/api/crews/", VALID_PAYLOAD)
    assert response.status_code == 403


def test_crew_create_return_201_for_admin(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post("/api/crews/", VALID_PAYLOAD)
    assert response.status_code == 201
