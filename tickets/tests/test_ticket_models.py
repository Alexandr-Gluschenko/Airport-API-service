import pytest
from django.db import IntegrityError

from tickets.models import Ticket


@pytest.mark.django_db
def test_ticket_created_with_valid_data(flight, order):
    ticket = Ticket.objects.create(
        row=1,
        seat=5,
        flight=flight,
        order=order
    )
    assert ticket.row == 1
    assert ticket.seat == 5
    assert ticket.flight == flight
    assert ticket.order == order

@pytest.mark.django_db
def test_second_ticket_with_same_data_send_integrity_error(flight, order):
    Ticket.objects.create(
        row=1,
        seat=5,
        flight=flight,
        order=order
    )
    with pytest.raises(IntegrityError):
        Ticket.objects.create(
            row=1,
            seat=5,
            flight=flight,
            order=order,
        )

@pytest.mark.django_db
def test_ticket_deleted_when_flight_deleted(flight, order):
    Ticket.objects.create(
        row=1,
        seat=5,
        flight=flight,
        order=order
    )

    flight.delete()

    assert Ticket.objects.count() == 0

@pytest.mark.django_db
def test_ticket_deleted_when_order_deleted(flight, order):
    Ticket.objects.create(
        row=1,
        seat=5,
        flight=flight,
        order=order
    )
    order.delete()

    assert Ticket.objects.count() == 0
