import requests
import os
from celery import shared_task


@shared_task
def send_reminder(chat_id, message):
    """
    Отправляет сообщение в Telegram через API.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    response = requests.get(url, params=params)
    return response.status_code
