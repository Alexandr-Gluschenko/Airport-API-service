import pytest
from django.contrib.auth.models import User

from orders.models import Order
from tickets.models import Ticket


@pytest.mark.django_db
def test_anonymous_doesnt_have_access(api_client):
    response = api_client.get('/api/tickets/')
    assert response.status_code == 401

@pytest.mark.django_db
def test_user_can_see_only_their_tickets(api_client, user, flight):
    other_user = User.objects.create_user(
        username="other_user",
        password="password123"
    )

    order_user = Order.objects.create(user=user)
    order_other = Order.objects.create(user=other_user)

    ticket_user = Ticket.objects.create(
        row=1,
        seat=5,
        flight=flight,
        order=order_user,
    )

    Ticket.objects.create(
        row=2,
        seat=6,
        flight=flight,
        order=order_other,
    )

    api_client.force_authenticate(user=user)
    response = api_client.get("/api/tickets/", format="json")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["id"] == ticket_user.id

@pytest.mark.django_db
def test_user_cannot_retrieve_other_users_ticket(api_client, user, flight):
    other_user = User.objects.create_user(
        username="other_user",
        password="password123"
    )

    order_user = Order.objects.create(user=user)
    order_other = Order.objects.create(user=other_user)

    other_ticket = Ticket.objects.create(
        row=1,
        seat=5,
        flight=flight,
        order=order_other,
    )

    api_client.force_authenticate(user=user)
    response = api_client.get(
        f"/api/tickets/{other_ticket.id}/",
        format="json"
    )

    assert response.status_code == 404
