import os

from celery import shared_task
from telegram import Bot


@shared_task
def send_reminder(chat_id, message):
    bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
    bot.send_message(chat_id=chat_id, text=message)
