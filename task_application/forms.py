from django import forms
from task_application.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'due_date', 'status', 'priority']