from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy, reverse


class CrudUsersTest(TestCase):
    def test_create_user(self):
        # Issue a POST request, create new user.
        response = Client().post(reverse_lazy('user_create'),
                                 {'username': 'john_smith',
                                  'password1': '12345',
                                  'password2': '12345',
                                  'first_name': 'Тест',
                                  'last_name': 'Тестович',
                                  })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

    def test_login_user(self):
        User = get_user_model()
        User.objects.create_user(username='john_smith', password='foo')
        response = Client().post(reverse_lazy('login'),
                                 {'username': 'john_smith',
                                  'password': 'foo',
                                  })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_update_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='john_smith', password='foo', first_name='john', last_name='smith')
        response = Client().post(reverse('user_update', kwargs={'pk': user.pk}),
                                 {'username': 'Terra',
                                  'first_name': 'Jack',
                                  'last_name': 'Richard',
                                  'password1': '12345',
                                  'password2': '12345',
                                  })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/')
        self.assertEqual(User.objects.get(pk=1).username, 'Terra')

    def test_delete_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='john_smith', password='foo', first_name='john', last_name='smith')
        responser = Client().post(reverse('user_delete', kwargs={'pk': 1}),
                                  )
        self.assertRedirects(responser, '/users/', 302)
