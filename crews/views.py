from rest_framework import viewsets

from config.permissions import IsAdminOrAuthenticatedReadOnly
from crews.models import Crew
from crews.serializers import CrewSerializer


# Create your views here.
class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
