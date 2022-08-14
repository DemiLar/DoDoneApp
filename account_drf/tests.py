import json
from django.urls import reverse

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from account.models import CustomizeUser


class MyProfileViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = CustomizeUser.objects.create_user(username='test',
                                                      password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('my_profile', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user'], 'test')

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse('my_profile', kwargs={'pk': self.user.pk}),
                                   {'work_position': 'developer', 'email': 'newtest@email'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content),
                         {'id': 1, 'user': 'test', 'work_position': 'developer', 'email': 'newtest@email'})

    def test_profile_update_by_random_user(self):
        random_user = CustomizeUser.objects.create_user(username='random test',
                                                        password='randompassword')
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse('my_profile', kwargs={'pk': self.user.pk}),
                                   {'work_position': 'hacker'})
        self.assertEqual(response.status_code, 401)
