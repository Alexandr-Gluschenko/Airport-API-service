from django.db import models

from airports.models import Airport


# Create your models here.
class Route(models.Model):
    source = models.ForeignKey(Airport,
                               on_delete=models.CASCADE,
                               related_name="routes_from",
                               )
    destination = models.ForeignKey(Airport,
                                    on_delete=models.CASCADE,
                                    related_name="routes_to")
    distance = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.source} -> {self.destination}"
