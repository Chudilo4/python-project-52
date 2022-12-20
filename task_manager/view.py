from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import gettext
from django.views import View
from . import forms
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy

menu = [{'title': 'Пользователи', 'url_name': 'users'},
        {'title': 'Статусы', 'url_name': 'home'},
        {'title': 'Метки', 'url_name': 'home'},
        {'title': 'Задачи', 'url_name': 'home'},
        ]


class IndexView(TemplateView):
    template_name = 'home.html'


class UsersView(TemplateView):
    pass


class UsersCreateView(TemplateView):
    pass


class UsersUpdateView(TemplateView):
    pass


class UsersDeleteView(TemplateView):
    pass


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
class LogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(self.get_success_url())
