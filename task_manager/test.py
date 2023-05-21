from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class TaskManager(TestCase):
    def setUp(self) -> None:
        user1 = User.objects.create(username="rafa", first_name='rafa',
                                    last_name='ddsf', password='S123qw4R')

    def test_delete_user(self):
        self.client.login(username='rafa', password='S123qw4R')
        url = reverse('user_delete', kwargs={'pk': 1})
        response = self.client.post(url)
        self.assertEquals(response.url, '/users/')
