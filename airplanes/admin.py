from django.contrib import admin
from .models import Airplane, AirPlaneType


@admin.register(AirPlaneType)
class AirplaneTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "airplane_type", "rows", "seats_in_rows"]
    list_filter = ["airplane_type",]
