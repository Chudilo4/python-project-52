from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, Http404
from django.views.generic import CreateView, UpdateView, DeleteView
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


class UsersView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'



class UsersCreateView(CreateView):
    template_name = 'users_create.html'
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)


class UsersUpdateView(UpdateView):
    model = User
    template_name = 'users_update.html'
    success_url = reverse_lazy('users')
    form_class = forms.RegisterUserForm


class UsersDeleteView(DeleteView):
    model = User
    template_name = 'users_delete.html'
    success_url = reverse_lazy('user_create')


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
