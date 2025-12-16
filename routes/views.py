from rest_framework import viewsets

from config.permissions import IsAdminOrAuthenticatedReadOnly
from routes.models import Route
from routes.serializers import RouteSerializer


# Create your views here.
class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAdminOrAuthenticatedReadOnly]