from ..models import Task, Status
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy, reverse


# class CrudTaskTest(TestCase):
#     def test_CRUD_task(self):
#         # Создаём юзера
#         User = get_user_model()
#         User.objects.create_user(username='john_smith', password='foo')
#         Status.objects.create(name='Новый тест')
#         status = Status.objects.get(pk=1)
#         user = User.objects.get(pk=1)
#         # Эмитируем работу браузера
#         response1 = Client()
#         # Логинимся
#         response1.login(username='john_smith', password='foo')
#         # Отправляем пост запрос на создание статуса
#         response1.post(reverse_lazy('task_create'),
#                        {'name': 'Тест',
#                         'description': 'Описание',
#                         'status': status.pk,
#                         'executor': user.pk,
#                         'labels': 1})
#         # Проверяем что Статус создался в БД
#         self.assertEqual(Task.objects.get(pk=1).name, 'Тест')
#         # Отправляем запрос на изменение статуса
#         response1.post(reverse('task_update', kwargs={'pk': 1}),
#                        {'name': 'Тест2',
#                         'description': 'Описание',
#                         'status': status.pk,
#                         'user': user.pk})
#         # Проверяем что объект в бд поменял значение
#         self.assertEqual(Task.objects.get(pk=1).name, 'Тест2')
#         # Отправляем запрос на удаление объекта из БД
#         response1.post(reverse('task_delete', kwargs={'pk': 1}))
#         # Проверяем кол-во объектов в БД
#         self.assertEqual(Task.objects.count(), 0)
