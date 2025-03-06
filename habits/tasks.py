from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from telegram_bot.tasks import send_reminder


@shared_task
def send_habit_reminders():
    """
    Отправляет напоминания о привычках.
    """
    habits = Habit.objects.filter(time__lte=timezone.now().time())
    for habit in habits:
        send_reminder.delay(
            habit.user.telegram_chat_id,
            f"Напоминание: {habit.action} в {habit.time} в {habit.place}",
        )
