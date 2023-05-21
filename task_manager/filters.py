import django_filters

from django import forms
from .models import Task


class TaskFilter(django_filters.FilterSet):
    my_task = django_filters.BooleanFilter(field_name='executor',
                                           label='Только свои задачи',
                                           widget=forms.CheckboxInput)

    class Meta:
        model = Task
        fields = ['status', 'my_task', 'label']
