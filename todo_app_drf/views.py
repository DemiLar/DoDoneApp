from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from todo_app.models import Task
from .serializers import TaskSerializer


class MyTasksViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['title']
    ordering_fields = ['due_date']

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(**{'user': self.request.user})

    @action(methods=['post'], detail=True)
    def mark_as_in_progress(self, request, pk=None):
        task = self.get_object()
        task.status = 'in_progress'
        if task.user == self.request.user:
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_blocked(self, request, pk=None):
        task = self.get_object()
        task.status = 'blocked'
        if task.user == self.request.user:
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def mark_as_finished(self, request, pk=None):
        task = self.get_object()
        task.status = 'finished'
        if task.user == self.request.user:
            task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data)
