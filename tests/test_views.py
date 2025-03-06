from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from habits.models import Habit
from users.models import User


class HabitViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Home",
            time="12:00",
            action="Read a book",
            duration=60,
        )

    def test_list_habits(self):
        url = reverse("habit-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)

    def test_create_habit(self):
        url = reverse("habit-list")
        data = {
            "place": "Park",
            "time": "18:00",
            "action": "Go for a walk",
            "duration": 30,
            "is_pleasant": False,
            "is_public": True,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_update_habit(self):
        url = reverse("habit-detail", args=[self.habit.id])
        data = {
            "place": "Home",
            "time": "12:00",
            "action": "Read a book",
            "duration": 90,
            "is_pleasant": False,
            "is_public": True,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.duration, 90)

    def test_delete_habit(self):
        url = reverse("habit-detail", args=[self.habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
