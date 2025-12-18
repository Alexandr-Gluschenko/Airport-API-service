import pytest

from orders.serializers import OrderReadSerializer, OrderWriteSerializer
from orders.views import OrderViewSet


@pytest.mark.django_db
def test_get_serializer_class_for_list():
    view = OrderViewSet()
    view.action = "list"
    assert view.get_serializer_class() == OrderReadSerializer

@pytest.mark.django_db
def test_get_serializer_class_for_create():
    view = OrderViewSet()
    view.action = "create"
    assert view.get_serializer_class() == OrderWriteSerializer
