from django.contrib import admin
from .models import Route


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ["source", "destination", "distance"]
    search_fields = ["source__name", "destination__name"]
