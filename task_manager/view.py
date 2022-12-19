from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.translation import gettext
from django.views import View
from . import forms

menu = [{'title': 'Пользователи', 'url_name': 'users'},
        {'title': 'Статусы', 'url_name': 'home'},
        {'title': 'Метки', 'url_name': 'home'},
        {'title': 'Задачи', 'url_name': 'home'},
        ]


class IndexView(View):
    def get(self, request, *args, **kwargs):
        out = gettext('Hello')
        return render(request, 'home.html', {'menu': menu})


class UsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users.html', {'menu': menu,
                                              'users': users,
                                              })


class UsersCreateView(View):
    def get(self, request, *args, **kwargs):
        form = forms.RegisterUserForm
        return render(request, 'users_create.html', {'menu': menu,
                                             'form': form,
                                             }
                      )

    def post(self, request, *args, **kwargs):
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users_create.html', {'menu': menu,
                                                         'form': form,
                                                         })


class UsersUpdateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'users_update.html', {'menu': menu})


class UsersDeleteView(View):

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        U = User.objects.get(id=user_id)
        if U:
            U.delete()
            return redirect('users')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'menu': menu})


class LogutView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'logout.html')
