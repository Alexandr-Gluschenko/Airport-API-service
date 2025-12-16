from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from config.permissions import IsTicketOwner
from tickets.models import Ticket
from tickets.serializers import TicketReadSerializer, TicketWriteSerializer


# Create your views here.
class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsTicketOwner]

    def get_queryset(self):
        return Ticket.objects.filter(order__user=self.request.user)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TicketReadSerializer
        return TicketWriteSerializer