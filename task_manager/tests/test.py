from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from task_manager.models import User, Label, Status, Task


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


class CRUD_Label_Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='123456789Zz')
        self.label = Label.objects.create(name='789')
        self.client.login(username='test', password='123456789Zz')

    def test_created_label(self):
        response = self.client.post(reverse('label_create'),
                                    {'name': '123'},
                                    follow=True)
        self.assertEqual(Label.objects.get(name='123').name, '123')
        self.assertRedirects(response, reverse_lazy('labels'))

    def test_update_label(self):
        response = self.client.post(reverse('label_update', kwargs={'pk': self.label.pk}),
                                    {'name': '456'},
                                    follow=True)
        self.assertEqual(Label.objects.get(name='456').name, '456')
        self.assertRedirects(response, reverse_lazy('labels'))

    def test_delete_label(self):
        response = self.client.post(reverse('label_delete', kwargs={'pk': self.label.pk}),
                                    follow=True)
        self.assertEqual(Label.objects.filter(name='789').count(), 0)
        self.assertRedirects(response, reverse_lazy('labels'))


class CRUD_Status_Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='123456789Zz')
        self.status = Status.objects.create(title='123')
        self.client.login(username='test', password='123456789Zz')

    def test_create_status(self):
        response = self.client.post(reverse_lazy('status_create'),
                                    {'title': '456'
                                     }, follow=True)
        self.assertEqual(Status.objects.get(title='456').title, '456')
        self.assertRedirects(response, reverse_lazy('status'))

    def test_update_status(self):
        response = self.client.post(reverse('status_update', kwargs={'pk': self.status.pk}),
                                    {'title': '456'}, follow=True)
        self.assertEqual(Status.objects.get(pk=self.status.pk).title, '456')
        self.assertRedirects(response, reverse_lazy('status'))

    def test_delete_status(self):
        response = self.client.post(reverse('status_delete', kwargs={'pk': self.status.pk}), follow=True)
        self.assertRedirects(response, reverse_lazy('status'))
        self.assertEqual(Status.objects.filter(title='123').count(), 0)


class CRUD_Task_Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='123456789Zz')
        self.executor = User.objects.create_user(username='test2', password='123456789Zz')
        self.status = Status.objects.create(title='123')
        self.label = Label.objects.create(name='789')
        self.label2 = Label.objects.create(name='777')
        self.new_task = self.label.task_set.create(title='qwe',
                                                   description='qwerty',
                                                   status=self.status,
                                                   executor=self.executor,
                                                   author=self.user)
        self.client.login(username='test', password='123456789Zz')

    def test_created_task(self):
        response = self.client.post(reverse_lazy('task_create'),
                                    {'title': 'Тестовая задача',
                                     'description': 'Описание тестовой задачи',
                                     'status': self.status.pk,
                                     'executor': self.executor.pk,
                                     'labels': self.label.pk
                                     }, follow=True)
        self.assertEqual(Task.objects.get(description='Описание тестовой задачи').title, 'Тестовая задача')
        self.assertRedirects(response, reverse_lazy('tasks'))

    def test_update_task(self):
        response = self.client.post(reverse('task_update', kwargs={'pk': self.new_task.pk}),
                                    {'title': 'Тестовая задача2',
                                     'description': 'Описание тестовой задачи2',
                                     'status': self.status.pk,
                                     'executor': self.executor.pk,
                                     'labels': self.label2.pk
                                     }, follow=True)
        self.assertEqual(Task.objects.get(pk=self.new_task.pk).title, 'Тестовая задача2')
        self.assertRedirects(response, reverse_lazy('tasks'))

    def test_task_delete(self):
        response = self.client.post(reverse('task_delete', kwargs={'pk': self.new_task.pk}),
                                    follow=True)
        self.assertEqual(Task.objects.filter(pk=self.new_task.pk).count(), 0)
        self.assertRedirects(response, reverse_lazy('tasks'))
