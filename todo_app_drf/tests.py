from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.utils import json

from task_application.models import Task


class MyTasksViewSetTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', work_position='tester',
                                                         password='testpassword',
                                                         email='test@example.com')
        self.user.save()
        self.timestamp = date.today()
        self.task = Task(user=self.user,
                         title='Test task',
                         content='This is test task',
                         created=self.timestamp,
                         due_date=self.timestamp,
                         done_date=self.timestamp + timedelta(days=1),
                         status='todo',
                         priority='medium',
                         importance=True
                         )
        self.task.save()

    def test_tasks_list_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('my_tasks'))
        self.assertEqual(response.status_code, 200)

    def test_tasks_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('my_tasks'))
        self.assertEqual(response.status_code, 401)

    def test_task_detail_retrieve(self):
        response = self.client.get(reverse('my_tasks', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test task')

    def test_task_update_by_owner(self):
        response = self.client.put(reverse('my_tasks', kwargs={'pk': self.task.pk}),
                                   {'title': 'test task 2', 'status': 'in_progress'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content),
                         {'id': self.task.pk, 'title': 'test task 2',
                          'status': 'in_progress'})

    def test_task_update_by_random_user(self):
        random_user = get_user_model().objects.create_user(username='random test',
                                                           password='randompassword')
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse('my_tasks', kwargs={'pk': self.task.pk}),
                                   {'title': 'hacker'})
        self.assertEqual(response.status_code, 401)
