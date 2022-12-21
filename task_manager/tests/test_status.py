from ..models import Status
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy, reverse


class CrudStatusTest(TestCase):
    def test_CRUD_status(self):
        # Создаём юзера
        User = get_user_model()
        User.objects.create_user(username='john_smith', password='foo')
        # Эмитируем работу браузера
        response1 = Client()
        # Логинимся
        response1.login(username='john_smith', password='foo')
        # Отправляем пост запрос на создание статуса
        response1.post(reverse_lazy('status_create'),
                       {'name': 'Тест'})
        # Проверяем что Статус создался в БД
        self.assertEqual(Status.objects.get(pk=1).name, 'Тест')
        # Отправляем запрос на изменение статуса
        response1.post(reverse('status_udate', kwargs={'pk': 1}),
                       {'name': 'Тест2'})
        # Проверяем что объект в бд поменял значение
        self.assertEqual(Status.objects.get(pk=1).name, 'Тест2')
        # Отправляем запрос на удаление объекта из БД
        response1.post(reverse('status_delete', kwargs={'pk': 1}))
        # Проверяем кол-во объектов в БД
        self.assertEqual(Status.objects.count(), 0)
