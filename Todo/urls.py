from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet

router = DefaultRouter()
router.register('todo', TodoItemViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]
