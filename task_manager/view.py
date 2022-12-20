from django.contrib.auth import authenticate, login
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
        form = forms.UpdateUserForm(instance=user)
        return render(request, 'users_update.html', {'menu': menu,
                                                     'form': form})
    def post(self, request, *args, **kwargs):
        user_pk = kwargs['pk']
        user = User.objects.get(pk=user_pk)
        form = forms.UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            return render(request, 'users_update.html', {'menu': menu,
                                                         'form': form})



class UsersDeleteView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        return render(request, 'users_delete.html', {'menu': menu,
                                                     'user': user})

    def post(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
            return redirect('users')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html', {'menu': menu})
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            redirect('login')
class LogutView(View):
    def post(self, request, *args, **kwargs):
        return render(request, 'logout.html')
