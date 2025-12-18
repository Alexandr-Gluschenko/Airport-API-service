import pytest

from orders.models import Order


@pytest.mark.django_db
def test_user_cannot_retrieve_other_user_order(api_client, another_user, user):
    other_order = Order.objects.create(user=another_user)
    api_client.force_authenticate(user=user)
    response = api_client.get(f"/api/orders/{other_order.id}/")
    assert response.status_code == 404

@pytest.mark.django_db
def test_user_cannot_see_other_orders(api_client, user, another_user):
    Order.objects.create(user=another_user)
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/orders/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_cannot_update_other_user_order(api_client, another_user, user):
    other_order = Order.objects.create(user=another_user)
    api_client.force_authenticate(user=user)
    response = api_client.patch(f"/api/orders/{other_order.id}/")
    assert response.status_code == 404

@pytest.mark.django_db
def test_user_cannot_delete_other_user_order(api_client, another_user, user):
    other_order = Order.objects.create(user=another_user)
    api_client.force_authenticate(user=user)
    response = api_client.delete(f"/api/orders/{other_order.id}/")
    assert response.status_code == 404