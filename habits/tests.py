from django.test import TestCase

from users.models import User

from .models import Habit


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.habit = Habit.objects.create(
            user=self.user,
            place="Home",
            time="12:00",
            action="Read a book",
            duration=60,
        )

    def test_habit_creation(self):
        self.assertEqual(self.habit.action, "Read a book")
        self.assertEqual(self.habit.duration, 60)
