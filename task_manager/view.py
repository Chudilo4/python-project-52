from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView

from task_manager.forms import UserCreateForm, StatusCreateForm, TaskCreateForm, LabelCreateForm
from task_manager.models import User, Status, Task, Label


class BaseView(TemplateView):
    template_name = 'task_manager/base.html'


class UsersListView(ListView):
    template_name = 'task_manager/users.html'
    model = User
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'task_manager/users_create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = User
    form_class = UserCreateForm
    template_name = 'task_manager/users_update.html'
    success_url = reverse_lazy('users')

    def has_permission(self):
        return self.request.user.pk == self.get_object().pk

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения другого пользователя.')
        return redirect('users')


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'task_manager/users_delete.html'
    success_url = reverse_lazy('users')

    def has_permission(self):
        return self.request.user.pk == self.get_object().pk

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для изменения другого пользователя.')
        return redirect('users')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, 'Невозможно удалить пользователя, потому что он используется')
            return redirect('users')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'task_manager/login.html'
    success_url = reverse_lazy('base')
    success_message = 'Вы залогинены'


class LogutUserView(SuccessMessageMixin, LogoutView):
    success_message = 'Вы разлогинены'


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'task_manager/status.html'
    context_object_name = 'status'
    login_url = reverse_lazy('login')


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'task_manager/status_create.html'
    success_url = reverse_lazy('status')
    login_url = reverse_lazy('login')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreateForm
    template_name = 'task_manager/status_create.html'
    success_url = reverse_lazy('status')
    login_url = reverse_lazy('login')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'task_manager/status_delete.html'
    success_url = reverse_lazy('status')
    login_url = reverse_lazy('login')


class TaskListView(LoginRequiredMixin, FilterView, ListView):
    model = Task
    template_name = 'task_manager/task.html'
    context_object_name = 'tasks'
    login_url = reverse_lazy('login')
    filterset_fields = ['status', 'executor', 'labels', 'author']


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_manager/task_create.html'
    success_url = reverse_lazy('tasks')

    def get_form_kwargs(self):
        kwargs = super(TaskCreateView, self).get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_manager/task_create.html'
    success_url = reverse_lazy('tasks')

    def get_form_kwargs(self):
        kwargs = super(TaskUpdateView, self).get_form_kwargs()
        kwargs['author'] = self.request.user
        return kwargs


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_manager/task_detail.html'


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_manager/task_delete.html'
    success_url = reverse_lazy('tasks')

    def has_permission(self):
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        messages.error(self.request, 'Задачу может удалить только её автор')
        return redirect('tasks')


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'task_manager/labels.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'task_manager/labels_create.html'
    success_url = reverse_lazy('labels')


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelCreateForm
    template_name = 'task_manager/label_update.html'
    success_url = reverse_lazy('labels')


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'task_manager/label_delete.html'
    success_url = reverse_lazy('labels')

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, 'Невозможно удалить метку, потому что она используется')
            return redirect('labels')
