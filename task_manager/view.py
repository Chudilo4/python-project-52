from django.shortcuts import render
from django.utils.translation import gettext
from django.views import View

menu = [{'title': 'Пользователи', 'url_name': 'users'},
        {'title': 'Статусы', 'url_name': '#'},
        {'title': 'Метки', 'url_name': '#'},
        {'title': 'Задачи', 'url_name': '#'},
        ]
class IndexView(View):
    def get(self, request, *args, **kwargs):
        out = gettext('Hello')
        return render(request, 'home.html', {'menu': menu})


class UsersView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users.html', {'menu': menu})


class UsersCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users_create.html', {'menu': menu})


class UsersUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users_update.html', {'menu': menu})


class UsersDeleteView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'users_delete.html', {'menu': menu})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'menu': menu})


class LogutView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'logout.html')
