from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,

)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from user.forms import RegisterForm, UserUpdateForm
from django.contrib.auth.views import LoginView
from .models import CustomUser


class HomeView(TemplateView):
    template_name = 'home.html'


class UserListView(ListView):
    template_name = 'users.html'
    model = CustomUser
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'user_create.html'
    model = CustomUser
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    success_message = 'Пользователь успешно зарегистрирован'


class UserUpdateView(SuccessMessageMixin,UpdateView):
    template_name = 'user_update.html'
    model = CustomUser
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_list')
    success_message = 'Пользователь успешно изменён'


class UserDeleteView(DeleteView):
    template_name = 'user_delete.html'
    model = CustomUser
    success_url = reverse_lazy('home')


class Login(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    success_message = 'Вы залогинены'



