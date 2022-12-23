from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, Http404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect
from django.utils.translation import gettext, gettext_lazy
from django.views import View
from django_filters.views import FilterView
from django.db import models

from . import forms
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .filters import TaskFilter
from .models import Status, Task, Label

menu = [{'title': 'Пользователи', 'url_name': 'users'},
        {'title': 'Статусы', 'url_name': 'statuses'},
        {'title': 'Метки', 'url_name': 'labels'},
        {'title': 'Задачи', 'url_name': 'task'},
        ]



class IndexView(TemplateView):
    '''Вьюха выводит главную страницу'''
    template_name = 'home.html'
    extra_context = {'menu': menu}


class UsersView(ListView):
    '''Вьюха выводит список пользователей'''
    model = User
    template_name = 'users.html'
    context_object_name = 'users'
    extra_context = {'menu': menu}


class UsersCreateView(SuccessMessageMixin, CreateView):
    '''Вьюха вывлдит регистрацию пользователя'''
    template_name = 'users_create.html'
    form_class = forms.RegisterUserForm
    success_url = reverse_lazy('login')
    extra_context = {'menu': menu}
    success_message = 'Пользователь успешно зарегистрирован'

    def form_valid(self, form):
        """Есди форма валидна то сохраняем объект в бд"""
        self.object = form.save()
        return super().form_valid(form)


class UsersUpdateView(SuccessMessageMixin, UpdateView):
    '''Вьюха выводит редактирование пользователя'''
    model = User
    template_name = 'users_update.html'
    success_url = reverse_lazy('users')
    form_class = forms.RegisterUserForm
    extra_context = {'menu': menu}
    success_message = 'Пользователь успешно изменён'

    def has_permission(self):
        '''Проверяет по pk пользователя который
        хочет внести изменения'''
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        '''Функция определяет значение has_permission
        в случае если True запрос проходит дальше
        False происходит редирект и выводи сообщение что
        у пользователя нет прав'''
        if not self.has_permission():
            messages.error(request, gettext_lazy('No permission'))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class UsersDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users_delete.html'
    success_url = reverse_lazy('users')
    extra_context = {'menu': menu}
    success_message = gettext('Пользователь успешно удалён')

    def has_permission(self):
        """Проверяет по pk пользователя который
        хочет внести изменения"""
        return self.get_object().pk == self.request.user.pk
    def dispatch(self, request, *args, **kwargs):
        """Функция определяет значение has_permission
        в случае если True запрос проходит дальше
        False происходит редирект и выводи сообщение что
        у пользователя нет прав"""
        if not self.has_permission():
            messages.error(request, gettext_lazy('No permission'))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class LoginUserView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_message = gettext('Вы залогинены')
    extra_context = {'menu': menu}
    error_message = gettext_lazy('An error has occurred.')

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, self.error_message)
        return self.render_to_response(self.get_context_data(form=form))


class LogoutUserView(SuccessMessageMixin, LogoutView):
    success_message = gettext('Вы разлогинены')

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return self.get_redirect_url() or self.get_default_redirect_url()


class StatusesView(LoginRequiredMixin, ListView):
    template_name = 'statuses.html'
    extra_context = {'menu': menu}
    model = Status
    context_object_name = 'status'
    login_url = reverse_lazy('login')


class StatusCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = forms.StatusForm
    template_name = 'status_create.html'
    extra_context = {'menu': menu}
    success_url = reverse_lazy('statuses')
    login_url = reverse_lazy('login')
    success_message = gettext_lazy('Status created successfully.')


class StatusUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'status_create.html'
    extra_context = {'menu': menu}
    success_url = reverse_lazy('statuses')
    form_class = forms.StatusForm
    model = Status
    login_url = reverse_lazy('login')
    success_message = gettext_lazy('Status changed successfully.')

    def has_permission(self):
        '''Проверяет по pk пользователя который
        хочет внести изменения'''
        return self.get_object().pk == self.request.user.pk and self.request.user.is_authenticated

    def dispatch(self, request, *args, **kwargs):
        '''Функция определяет значение has_permission
        в случае если True запрос проходит дальше
        False происходит редирект и выводи сообщение что
        у пользователя нет прав'''
        if not self.has_permission():
            messages.error(request, gettext_lazy('No permission'))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class StatusDelete(LoginRequiredMixin, DeleteView):
    template_name = 'status_delete.html'
    model = Status
    success_url = reverse_lazy('statuses')
    extra_context = {'menu': menu}
    login_url = reverse_lazy('login')


class TaskView(LoginRequiredMixin, FilterView, ListView):
    template_name ='task.html'
    model = Task
    context_object_name = 'tasks'
    extra_context = {'menu': menu}
    login_url = reverse_lazy('login')
    filterset_class = TaskFilter


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    form_class = forms.TaskForm
    extra_context = {'menu': menu}
    success_url = reverse_lazy('task')
    login_url = reverse_lazy('login')
    success_message = gettext_lazy('Task created successfully.')



class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task')
    extra_context = {'menu': menu}

    def has_permission(self):
        '''Проверяет по pk пользователя который
        хочет внести изменения'''
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        '''Функция определяет значение has_permission
        в случае если True запрос проходит дальше
        False происходит редирект и выводи сообщение что
        у пользователя нет прав'''
        if not self.has_permission():
            messages.error(request, gettext_lazy('No permission'))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'task_create.html'
    extra_context = {'menu': menu}
    success_url = reverse_lazy('task')
    form_class = forms.TaskForm
    model = Task
    success_message = gettext_lazy('Task changed successfully.')
    login_url = reverse_lazy('login')

    def has_permission(self):
        '''Проверяет по pk пользователя который
        хочет внести изменения'''
        return self.get_object().pk == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        '''Функция определяет значение has_permission
        в случае если True запрос проходит дальше
        False происходит редирект и выводи сообщение что
        у пользователя нет прав'''
        if not self.has_permission():
            messages.error(request, gettext_lazy('No permission'))
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class TaskShowView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_show.html'
    login_url = reverse_lazy('login')


class LabelsView(ListView):
    template_name = 'labels.html'
    model = Label
    context_object_name = 'labels'
    extra_context = {'menu': menu}


class LabelCreateView(SuccessMessageMixin, CreateView):
    form_class = forms.LabelForm
    template_name = 'labels_create.html'
    success_url = reverse_lazy('labels')
    success_message = gettext_lazy('Labels create!')
    extra_context = {'menu': menu}


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'label_update.html'
    extra_context = {'menu': menu}
    success_url = reverse_lazy('labels')
    form_class = forms.LabelForm
    model = Label
    success_message = gettext_lazy('label changed successfully.')
    login_url = reverse_lazy('login')


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'label_delete.html'
    success_url = reverse_lazy('labels')
    extra_context = {'menu': menu}

