from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView

urlpatterns = [
    path(
        "register/", RegisterView.as_view(), name="register"
    ),  # Маршрут для регистрации
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # Маршрут для получения токена
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Маршрут для обновления токена
]
