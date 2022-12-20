from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, AuthenticationForm


class RegisterUserForm(forms.ModelForm):
    # Прописываем поля для нашей регистрации
    first_name = forms.CharField(max_length=150,
                                 label='Имя',)
    last_name = forms.CharField(max_length=150,
                                label='Фамилия',)
    username = forms.CharField(max_length=150,
                               label='Имя пользователя',)
    password1 = forms.CharField(label='Пароль',)
    password2 = forms.CharField(label='Подтверждение пароля',)
    class Meta:
        # Для сохранения в таблицу USER используем модель User
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль',)
    password2 = forms.CharField(label='Подтверждение пароля',)
    class Meta:
        # Для сохранения в таблицу USER используем модель User
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
