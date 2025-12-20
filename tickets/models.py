from django.db import models

from flights.models import Flight
from orders.models import Order


# Create your models here.
class Ticket(models.Model):
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()
    flight = models.ForeignKey(Flight,
                               on_delete=models.CASCADE,
                               related_name="tickets")

    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name="tickets")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["row", "seat", "flight"],
                name="unique_seat_per_flight"
            )
        ]
