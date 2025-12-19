import pytest

from tickets.models import Ticket
from tickets.serializers import TicketReadSerializer, TicketWriteSerializer


@pytest.mark.django_db
def test_serializer_ticket_read_is_valid(flight, order):
    ticket = Ticket.objects.create(
        row=1,
        seat=5,
        flight=flight,
        order=order,
    )
    serializer = TicketReadSerializer(ticket)
    data = serializer.data

    assert data["id"] == ticket.id
    assert data["flight"] == flight.id
    assert data["row"] == 1
    assert data["seat"] == 5
    assert "order" not in data

@pytest.mark.django_db
def test_serializer_ticket_write_is_valid(flight, order):
    data = {
        "row": 1,
        "seat": 5,
        "flight": flight.id,
    }
    serializer = TicketWriteSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    ticket = serializer.save(order=order)
    assert Ticket.objects.count() == 1
    assert ticket.flight == flight
    assert ticket.order == order
    assert ticket.row == 1
    assert ticket.seat == 5