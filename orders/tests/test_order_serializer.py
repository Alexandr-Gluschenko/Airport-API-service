import pytest
from orders.serializers import OrderWriteSerializer, OrderReadSerializer


@pytest.mark.django_db
def test_valid_data_with_empty_fields():
    serializer = OrderWriteSerializer(data={})
    assert serializer.is_valid(), serializer.errors

@pytest.mark.django_db
def test_order_read_serializer_returns_expected_fields(order):
    serializer = OrderReadSerializer(order)

    data = serializer.data

    assert "id" in data
    assert "created_at" in data
    assert "user" not in data

    assert data["id"] == order.id
