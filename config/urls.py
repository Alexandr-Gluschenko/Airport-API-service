from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from airplanes.views import AirplaneViewSet
from airports.views import AirportViewSet
from crews.views import CrewViewSet
from flights.views import FlightViewSet
from orders.views import OrderViewSet
from routes.views import RouteViewSet
from tickets.views import TicketViewSet


router = DefaultRouter()
router.register("airplanes", AirplaneViewSet, basename="airplane")
router.register("airports", AirportViewSet, basename="airport")
router.register("crews", CrewViewSet, basename="crew")
router.register("flights", FlightViewSet, basename="flight")
router.register("orders", OrderViewSet, basename="order")
router.register("routes", RouteViewSet, basename="route")
router.register("tickets", TicketViewSet, basename="ticket")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
