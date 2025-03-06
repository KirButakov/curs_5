# Трекер привычек

Проект представляет собой трекер привычек, который позволяет пользователям создавать, редактировать и удалять привычки. Привычки могут быть публичными или приватными, а также могут быть связаны с другими привычками. Пользователи могут регистрироваться и авторизовываться через JWT. Для напоминаний о привычках используется Telegram-бот, который отправляет уведомления через Celery.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/KirButakov/curs_5
   cd habbit_tracker

2. Создайте и активируйте виртуальное окружение:

- python -m venv venv

- source venv/bin/activate  # Для Linux/Mac

- venv\Scripts\activate     # Для Windows

3. Установите зависимости:

- pip install -r requirements.txt

4. Создайте файл .env и добавьте туда необходимые переменные:

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
CELERY_BROKER_URL=redis://redis:6379/0

DATABASE_NAME=habbit_tracker
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_HOST=db
DATABASE_PORT=5432

5. Запустите сервер:

- python manage.py runserver

6. Запустите Celery:

- celery -A habbit_tracker worker --loglevel=info

# Использование 

1. Регистрация пользователя

curl -X POST http://localhost:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "testpass"}'
2. Авторизация и получение токена

curl -X POST http://localhost:8000/api/auth/token/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass"}'
3. Создание привычки

curl -X POST http://localhost:8000/api/habits/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <ваш-токен>" \
-d '{
  "place": "Home",
  "time": "12:00",
  "action": "Read a book",
  "duration": 60,
  "is_pleasant": false,
  "is_public": true
}'
4. Получение списка привычек

curl -X GET http://localhost:8000/api/habits/ \
-H "Authorization: Bearer <ваш-токен>"

## Документация API

Документация API доступна через Swagger и ReDoc:

- **Swagger:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **ReDoc:** [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

Для ручного описания эндпоинтов используется библиотека `drf-yasg`.