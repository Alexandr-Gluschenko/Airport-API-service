from django.core.exceptions import ValidationError
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

    def clean(self):
        if self.departure_time >= self.arrival_time:
            raise ValidationError(
                {"arrival_time": "Arrival time"
                                 " must be later than departure time."}
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return (f"{self.route}"
                f" {self.airplane} {self.departure_time} {self.arrival_time}")
