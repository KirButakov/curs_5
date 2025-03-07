from celery import Celery
from celery.schedules import crontab

app = Celery("habbit_tracker")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.beat_schedule = {
    "send-habit-reminders": {
        "task": "habits.tasks.send_habit_reminders",
        "schedule": crontab(minute="*/1"),
    },
}
app.autodiscover_tasks()
