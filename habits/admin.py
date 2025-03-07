from django.contrib import admin

from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ("action", "place", "time", "user")
    list_filter = ("is_pleasant", "is_public")
    search_fields = ("action", "place")
