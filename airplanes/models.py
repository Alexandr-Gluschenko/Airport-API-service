from django.db import models, IntegrityError


# Create your models here.
class AirPlaneType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Airplane(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rows = models.PositiveIntegerField()
    seats_in_rows = models.PositiveIntegerField()
    airplane_type = models.ForeignKey(AirPlaneType,
                                      on_delete=models.CASCADE,
                                      null=False,
                                      related_name="airplanes")

    def __str__(self):
        return self.name
