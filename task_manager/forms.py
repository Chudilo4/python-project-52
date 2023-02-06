from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.models import *


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['title']


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'executor', 'labels']

    def __init__(self, *args, **kwargs):
        author = kwargs.pop('author', None)
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        self.instance.author = author


class LabelCreateForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
