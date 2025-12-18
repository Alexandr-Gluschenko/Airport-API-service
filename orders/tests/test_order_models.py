import pytest

from conftest import api_client
from orders.models import Order


@pytest.mark.django_db
def test_create_order_anonymous(api_client):
    response = api_client.get("/api/orders/")
    assert response.status_code == 401

@pytest.mark.django_db
def test_create_order_authenticated_user(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/orders/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_order_str_format(order):
    assert str(order) == f"Order #{order.id}"

@pytest.mark.django_db
def test_order_list_returns_user_orders(api_client, order, user):
    assert order.user == user

    api_client.force_authenticate(user=user)
    response = api_client.get("/api/orders/")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == order.id


