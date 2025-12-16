from rest_framework import viewsets

from config.permissions import IsAdminOrAuthenticatedReadOnly
from flights.models import Flight
from flights.serializers import (FlightWriteSerializer,
                                 FlightReadSerializer)


# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related("route", "airplane").prefetch_related("crew")
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FlightReadSerializer
        return FlightWriteSerializer