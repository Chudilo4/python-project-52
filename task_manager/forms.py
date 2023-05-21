from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

from MyCustomUser.models import CustomUser
from .models import Status, Task, Label


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Ваш пароль должен содержать как минимум 3 символа.',
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text='Для подтверждения введите, пожалуйста, пароль ещё раз.',
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'Пароли не совпадают',
                code="password_mismatch",
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class LabelCreateForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
