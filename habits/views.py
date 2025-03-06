from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .serializers import HabitSerializer
from .validators import validate_habit_fields


class HabitPagination(pagination.PageNumberPagination):
    page_size = 5


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
