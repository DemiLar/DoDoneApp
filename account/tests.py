from datetime import date

from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase


class SigninTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         password='testpassword',
                                                         email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='testpassword')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='testpassword')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrongtestpassword')
        self.assertFalse(user is not None and user.is_authenticated)


class ProfileTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test',
                                                         first_name='test',
                                                         last_name='test',
                                                         email='test@example.com',
                                                         work_position='tester',
                                                         password='testpassword',
                                                         )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_profile_detail(self):
        self.assertEqual(self.user.username, 'test')
        self.assertEqual(self.user.first_name, 'test')
        self.assertEqual(self.user.last_name, 'test')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.work_position, 'tester')

    def test_profile_update(self):
        self.user.username = 'new test name'
        self.user.first_name = 'New test'
        self.user.last_name = 'new test'
        self.user.email = 'newtest@example.com'
        self.user.work_position = 'developer'
        self.user.save()
        self.assertEqual(self.user.username, 'new test name')
        self.assertEqual(self.user.first_name, 'New test')
        self.assertEqual(self.user.last_name, 'new test')
        self.assertEqual(self.user.email, 'newtest@example.com')
        self.assertEqual(self.user.work_position, 'developer')