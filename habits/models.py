from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habits")
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False)
    related_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    frequency = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(7)]
    )
    reward = models.CharField(max_length=255, blank=True)
    duration = models.PositiveIntegerField(validators=[MaxValueValidator(120)])
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.action} at {self.time} in {self.place}"
