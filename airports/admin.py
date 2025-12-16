from django.contrib import admin
from .models import Airport


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "closest_big_city"]
    search_fields = ["name", "closest_big_city"]
