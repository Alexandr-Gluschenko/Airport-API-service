from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from config.permissions import IsOrderOwner
from orders.models import Order
from orders.serializers import OrderWriteSerializer, OrderReadSerializer


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOrderOwner]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderReadSerializer
        return OrderWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)