from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Status, Task, Label
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']


class LabelCreateForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
