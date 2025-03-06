from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User  # Импортируем кастомную модель пользователя

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Создаем пользователя через сериализатор
        response = super().create(request, *args, **kwargs)

        # Получаем только что созданного пользователя
        user = User.objects.get(username=request.data["username"])

        # Создаем JWT токены для пользователя
        refresh = RefreshToken.for_user(user)

        # Возвращаем в ответе access и refresh токены
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )
