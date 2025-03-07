def get_user_by_chat_id(chat_id):
    from users.models import User

    return User.objects.filter(telegram_chat_id=chat_id).first()
