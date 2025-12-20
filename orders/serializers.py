from rest_framework import serializers
from orders.models import Order


class OrderWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = []


class OrderReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "created_at",]
