from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from task_manager.models import User


class CRUD_Users_Test(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.user = User.objects.create_user(username='test2', password='123456789Zz')

    def test_create_user(self):
        response = self.client.post(reverse_lazy('users_create'),
                                    {'username': 'test',
                                     'first_name': 'name',
                                     'last_name': 'famili',
                                     'password1': '123456789Zz',
                                     'password2': '123456789Zz'
                                     }, follow=True)
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertEqual(User.objects.get(username='test').username, 'test')

    def test_read_user(self):
        response = self.client.post(reverse_lazy('login'),
                                    {'username': 'test2',
                                     'password': '123456789Zz'
                                     }, follow=True)
        self.assertRedirects(response, reverse_lazy('base'))

    def test_update_user(self):
        self.client.login(username='test2', password='123456789Zz')
        response = self.client.post(reverse('users_update', kwargs={'pk': self.user.pk}),
                                    {'username': 'test3',
                                     'password1': '123456789Zz',
                                     'password2': '123456789Zz'
                                     }, follow=True)
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertEqual(User.objects.get(username='test3').username, 'test3')

    def test_delete_user(self):
        self.client.login(username='test2', password='123456789Zz')
        response = self.client.post(reverse('users_delete', kwargs={'pk': self.user.pk}),
                                    follow=True)
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertEqual(User.objects.filter(pk=self.user.pk).count(), 0)