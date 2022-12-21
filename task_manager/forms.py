from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, User
from . import models


class RegisterUserForm(forms.ModelForm):
    # Прописываем поля для нашей регистрации
    first_name = forms.CharField(max_length=150,
                                 label='Имя',)
    last_name = forms.CharField(max_length=150,
                                label='Фамилия',)
    username = forms.CharField(max_length=150,
                               label='Имя пользователя',
                               help_text='Обязательное поле. Не более 150'
                                         ' символов. Только буквы,'
                                         ' цифры и символы @/./+/-/_.')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(),
                                help_text='Ваш пароль должен '
                                          'содержать как минимум 3 символа.')
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(),
                                help_text='Для подтверждения введите,'
                                          ' пожалуйста, пароль ещё раз.')

    class Meta:
        # Для сохранения в таблицу USER используем модель User
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user

    def clean(self):
        cleaned_data = super(RegisterUserForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Password did not match.')
        return cleaned_data


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class StatusForm(forms.ModelForm):
    class Meta:
        model = models.Status
        fields = ['name']
