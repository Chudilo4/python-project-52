from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username',]
