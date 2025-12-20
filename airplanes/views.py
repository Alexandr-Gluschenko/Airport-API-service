from rest_framework import viewsets

from airplanes.models import Airplane
from airplanes.serializers import (AirplaneWriteSerializer,
                                   AirplaneReadSerializer,
                                   AirplaneTypeSerializer)
from config.permissions import IsAdminOrAuthenticatedReadOnly


# Create your views here.
class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneTypeSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.select_related("airplane_type")
    permission_classes = [IsAdminOrAuthenticatedReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return AirplaneReadSerializer
        return AirplaneWriteSerializer
