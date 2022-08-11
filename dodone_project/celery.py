import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dodone_project.settings')

app = Celery('dodone_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send-reminder-every-day-at-8am': {
        'task': 'task_application.tasks.send_task_with_tomorrow_deadline',
        'schedule': crontab(minute=0, hour=8),
    },
}

app.conf.beat_schedule = {
    'send-reminder-every-saturday-at-9am': {
        'task': 'task_application.tasks.send_completed_tasks',
        'schedule': crontab(minute='0', hour='9', day_of_week='sat'),
    },
}

