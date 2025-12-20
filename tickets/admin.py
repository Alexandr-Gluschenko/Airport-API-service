from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["id", "row", "seat", "flight", "order"]
    list_filter = ["flight"]
    search_fields = ["flight__id"]
