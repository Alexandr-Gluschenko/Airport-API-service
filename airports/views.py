from rest_framework import viewsets

from airports.models import Airport
from airports.serializers import AirportSerializer
from config.permissions import IsAdminOrAuthenticatedReadOnly


# Create your views here.
class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]