from django.contrib import admin
from .models import Crew


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    search_fields = ["first_name", "last_name"]
