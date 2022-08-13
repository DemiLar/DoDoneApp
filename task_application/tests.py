from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Task


class TaskTests(TestCase):
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

    def tearDown(self):
        self.user.delete()

    def test_read_task(self):
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.title, 'Test task')
        self.assertEqual(self.task.content, 'This is test task')
        self.assertEqual(self.task.created, self.timestamp)
        self.assertEqual(self.task.due_date, self.timestamp)
        self.assertEqual(self.task.done_date, self.timestamp + timedelta(days=1))
        self.assertEqual(self.task.status, 'todo')
        self.assertEqual(self.task.priority, 'medium')
        self.assertEqual(self.task.importance, 1)

    def test_update_task(self):
        self.task.title = 'New test title'
        self.task.content = 'New test task'
        self.task.due_date = self.timestamp + timedelta(days=2)
        self.task.status = 'in_progress'
        self.task.priority = 'high'
        self.task.importance = False
        self.task.save()
        self.assertEqual(self.task.title, 'New test title')
        self.assertEqual(self.task.content, 'New test task')
        self.assertEqual(self.task.due_date, self.timestamp + timedelta(days=2))
        self.assertEqual(self.task.status, 'in_progress')
        self.assertEqual(self.task.priority, 'high')
        self.assertEqual(self.task.importance, 0)


class AllTasksViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         password='testpassword',
                                                         email='test2@example.com')
        self.user.save()
        self.timestamp = date.today()
        self.client.login(username='test', password='testpassword')

    def tearDown(self):
        self.user.delete()

    def test_no_tasks(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_one_task(self):
        self.task1 = Task(user=self.user,
                          title='Test task1',
                          content='This is test task1',
                          created=self.timestamp,
                          due_date=self.timestamp,
                          done_date=self.timestamp + timedelta(days=2),
                          status='todo',
                          priority='medium',
                          importance=True
                          )
        self.task1.save()
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)