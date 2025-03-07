from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated
from .pagination import HabitPagination
from .models import Habit
from .serializers import HabitSerializer
from .validators import validate_habit_fields
from rest_framework.decorators import action
from rest_framework.response import Response


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Habit.objects.all()
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        validate_habit_fields(serializer.validated_data)
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def public(self, request):
        """
        Возвращает список публичных привычек.
        """
        habits = Habit.objects.filter(is_public=True)
        page = self.paginate_queryset(habits)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(habits, many=True)
        return Response(serializer.data)
