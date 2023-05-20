import django_filters

from django import forms
from .models import Task


class TaskFilter(django_filters.FilterSet):
    my_task = django_filters.BooleanFilter(field_name='author',
                                           label='Только свои задачи',
                                           widget=forms.CheckboxInput)

    class Meta:
        model = Task
        fields = ['status', 'executor', 'label', 'my_task']
