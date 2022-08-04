from todo_app.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'content', 'due_date', 'status', 'priority', 'importance', 'id']
