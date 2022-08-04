from django import forms
from todo_app.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'due_date', 'status', 'priority']