from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,

)
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from task_manager.forms import UserCreateForm, UserUpdateForm
from django.contrib.auth.views import LoginView

class HomeView(TemplateView):
    template_name = 'home.html'


class UserListView(ListView):
    template_name = 'users.html'
    model = User
    context_object_name = 'users'


class UserCreateView(CreateView):
    template_name = 'user_create.html'
    model = User
    form_class = UserCreateForm
    success_url = reverse_lazy('user_list')


class UserUpdateView(UpdateView):
    template_name = 'user_update.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    template_name = 'user_delete.html'
    model = User
    success_url = reverse_lazy('home')


class Login(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')
