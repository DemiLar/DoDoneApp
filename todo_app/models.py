from datetime import date

from django.db import models
from django.conf import settings


CHOICE_PRIORITY = [
                   ('Low', 'low'),
                   ('Medium', 'medium'),
                   ('High', 'high')
                ]

CHOICE_STATUS = [
                 ('ToDo', 'todo'),
                 ('In_progress', 'in_progress'),
                 ('Blocked', 'blocked'),
                 ('Finished', 'finished')
                ]


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=date.today().strftime('%B %d, %Y'))
    status = models.CharField(choices=CHOICE_STATUS, max_length=15, default='todo')
    priority = models.CharField(choices=CHOICE_PRIORITY, max_length=7, default='medium')
    importance = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'

