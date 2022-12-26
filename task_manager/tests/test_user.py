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
        c = Client()
        c.login(username='john_smith', password='foo')
        c.post('/users/1/update/', {'username': 'Tera',
                                    'first_name': 'jo',
                                    'last_name': 'Totot',
                                    'password1': 1234,
                                    'password2': 1234})
        self.assertEqual(User.objects.get(pk=1).username, 'Tera')

    def test_delete_user(self):
        User = get_user_model()
        User.objects.create_user(username='john_smith', password='foo', first_name='john', last_name='smith')
        response = Client()
        response.login(username='john_smith', password='foo')
        code = response.post(reverse('user_delete', kwargs={'pk': 1}))
        self.assertEqual(User.objects.count(), 0)
        self.assertRedirects(code, '/users/', 302)