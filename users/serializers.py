from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Используйте get_user_model(), если это CustomUser
        fields = ("id", "username", "email", "password", "groups", "user_permissions")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Убедитесь, что создаете пользователя через create_user()
        user = get_user_model().objects.create_user(**validated_data)
        return user
