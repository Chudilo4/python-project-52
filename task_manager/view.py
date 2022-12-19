from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.translation import gettext
from django.views import View
from . import forms
from django.urls import reverse_lazy

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
        user = User.objects.get(pk=kwargs['pk'])
        form = forms.UpdateUserForm({'first_name': user.first_name,
                                     'last_name': user.last_name,
                                     'username': user.username})
        return render(request, 'users_update.html', {'menu': menu,
                                                     'form': form})
    def post(self, request, *args, **kwargs):
        form = forms.UpdateUserForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=kwargs['pk'])
            User.objects.update()
            return redirect('users')
        else:
            return render(request, 'users_update.html', {'menu': menu,
                                                         'form': form})



class UsersDeleteView(View):

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
            return redirect('users')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'menu': menu})


class LogutView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'logout.html')
