from django.test import TestCase
from rest_framework.exceptions import ValidationError

from habits.validators import validate_habit_fields


class HabitValidatorsTest(TestCase):
    def test_validate_habit_fields(self):
        data = {"related_habit": 1, "reward": "Chocolate"}
        with self.assertRaises(ValidationError):
            validate_habit_fields(data)
