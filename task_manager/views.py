from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from task_manager.forms import (
    RegisterForm, UserUpdateForm,
    StatusCreateForm, TaskCreateForm,
    LabelCreateForm)
from django.contrib.auth.views import LoginView, LogoutView

from .filters import TaskFilter
from .models import Status, Task, Label
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = 'home.html'


class UserListView(ListView):
    template_name = 'users.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'user_create.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'user_update.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_list')
    success_message = 'Пользователь успешно изменен'
    permission_denied_message = 'У вас нет прав для изменения другого пользователя.'
    redirect_field_name = reverse_lazy('users')

    def has_permission(self, *args, **kwargs):
        return self.request.user == self.get_object()

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения другого пользователя.')
        return redirect('user_list')


class UserDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'user_delete.html'
    model = User
    success_url = reverse_lazy('user_list')
    success_message = 'Пользователь успешно удалён'

    def has_permission(self, *args, **kwargs):
        return self.request.user == self.get_object() and len(self.request.user.task_author.all()) == 0

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения другого пользователя.')
        return redirect('user_list')


class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    success_message = 'Вы залогинены'


class Logout(LogoutView):

    def get_success_url(self):
        messages.success(self.request, 'Вы разлогинены')
        return self.get_redirect_url() or self.get_default_redirect_url()


class StatusListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    template_name = 'status_list.html'
    model = Status
    context_object_name = 'status'
    login_url = reverse_lazy('login')


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'status_create.html'
    form_class = StatusCreateForm
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно создан'
    login_url = reverse_lazy('login')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    template_name = 'status_update.html'
    form_class = StatusCreateForm
    success_url = reverse_lazy('status_list')
    success_message = 'Статус успешно изменён'
    login_url = reverse_lazy('login')


class StatusDeleteView(LoginRequiredMixin,
                       PermissionRequiredMixin,
                       SuccessMessageMixin,
                       DeleteView):
    template_name = 'status_delete.html'
    model = Status
    success_message = 'Статус успешно удалён'
    success_url = reverse_lazy('status_list')
    login_url = reverse_lazy('login')

    def has_permission(self):
        return len(self.get_object().task_status.all()) == 0

    def handle_no_permission(self):
        messages.error(self.request,
                       'Невозможно удалить статус, потому что он используется')
        return redirect('status_list')


class TaskListView(LoginRequiredMixin, FilterView, ListView):
    template_name = 'task_list.html'
    model = Task
    filterset_class = TaskFilter
    login_url = reverse_lazy('login')


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("task_list")
    success_message = 'Задача успешно создана'
    login_url = reverse_lazy('login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            messages.success(self.request, self.success_message)
            return HttpResponseRedirect(self.success_url)
        return render(request, 'task_create.html', {'form': form})


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'task_update.html'
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('task_list')
    success_message = 'Задача успешно изменена'
    login_url = reverse_lazy('login')


class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'task_delete.html'
    model = Task
    success_url = reverse_lazy('task_list')
    login_url = reverse_lazy('login')

    def has_permission(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, 'Задачу может удалить только её автор')
        return redirect('task_list')


class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = 'task_detail.html'
    model = Task
    context_object_name = 'task'
    login_url = reverse_lazy('login')


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'label_list.html'
    login_url = reverse_lazy('login')


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'label_create.html'
    success_url = reverse_lazy('label_list')
    login_url = reverse_lazy('login')


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'label_update.html'
    success_url = reverse_lazy('label_list')
    login_url = reverse_lazy('login')


class LabelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Label
    template_name = 'label_delete.html'
    success_url = reverse_lazy('label_list')
    login_url = reverse_lazy('login')

    def has_permission(self):
        return len(self.get_object().task_set.all()) == 0

    def handle_no_permission(self):
        messages.error(self.request,
                       'Невозможно удалить метку, потому что она используется')
        return redirect('label_list')
