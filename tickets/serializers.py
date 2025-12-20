from rest_framework import serializers

from tickets.models import Ticket


class TicketWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["flight", "row", "seat"]


class TicketReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "flight", "row", "seat"]
