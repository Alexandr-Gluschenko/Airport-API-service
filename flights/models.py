from django.db import models

from airplanes.models import Airplane
from crews.models import Crew
from routes.models import Route


class Flight(models.Model):
    crew = models.ManyToManyField(Crew, related_name="flights")

    route = models.ForeignKey(Route,
                              on_delete=models.CASCADE,
                              related_name="flights")

    airplane = models.ForeignKey(Airplane,
                                 on_delete=models.CASCADE,
                                 related_name="flights")

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.route} {self.airplane} {self.departure_time} {self.arrival_time}"
