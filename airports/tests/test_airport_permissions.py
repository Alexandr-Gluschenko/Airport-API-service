def test_airport_list_forbidden_for_anonymous(api_client):
    response = api_client.get('/api/airports/')
    assert response.status_code == 401

def test_airport_list_return_200_for_authenticated_user(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get('/api/airports/')
    assert response.status_code == 200

def test_airport_create_return_401_for_anonymous_user(api_client):
    response = api_client.post('/api/airports/')
    assert response.status_code == 401

def test_airport_create_return_403_for_authenticated_user(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post('/api/airports/')
    assert response.status_code == 403

def test_airport_create_return_201_for_admin(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post(
        "/api/airports/",
        {"name": "Heathrow",
         "closest_big_city": "London"}
    )
    assert response.status_code == 201