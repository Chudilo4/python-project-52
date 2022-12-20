from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, Http404
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.utils.translation import gettext, gettext_lazy
from django.views import View
from . import forms
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

menu = [{'title': 'Пользователи', 'url_name': 'users'},
        {'title': 'Статусы', 'url_name': 'home'},
        {'title': 'Метки', 'url_name': 'home'},
        {'title': 'Задачи', 'url_name': 'home'},
        ]


class IndexView(TemplateView):
    template_name = 'home.html'
    extra_context = {'menu': menu}


class UsersView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'
    extra_context = {'menu': menu}



class UsersCreateView(CreateView):
    template_name = 'users_create.html'
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('login')
    extra_context = {'menu': menu}


    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super().form_valid(form)


class UsersUpdateView(UpdateView):
    model = User
    template_name = 'users_update.html'
    success_url = reverse_lazy('users')
    form_class = forms.RegisterUserForm
    extra_context = {'menu': menu}


class UsersDeleteView(DeleteView):
    model = User
    template_name = 'users_delete.html'
    success_url = reverse_lazy('user_create')
    extra_context = {'menu': menu}


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_message = gettext_lazy('You are log in.')
    extra_context = {'menu': menu}
    error_message = gettext_lazy('An error has occurred.')

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        messages.success(self.request, self.success_message)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, self.error_message)
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(self.get_success_url())
