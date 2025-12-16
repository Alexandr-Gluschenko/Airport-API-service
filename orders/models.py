from django.db import models
from django.conf import settings

# Create your models here.
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="orders")

    def __str__(self):
        return f"Order #{self.id}"