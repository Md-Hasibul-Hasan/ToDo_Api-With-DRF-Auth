from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TodoItem
from .serializers import TodoItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import TodoPagination
from .permissions import IsOwner

class TodoItemViewSet(viewsets.ModelViewSet):
    serializer_class = TodoItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_completed']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at']
    pagination_class = TodoPagination

    def get_queryset(self):
        return TodoItem.objects.filter(
            user=self.request.user
        ).order_by('-created_at')
        # return TodoItem.objects.all() # for testing purpose

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
