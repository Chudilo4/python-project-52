import django_filters

from django import forms
from .models import Task, Label


class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['status', 'label']

    @property
    def qs(self):
        parent = super().qs
        if self.request.GET.get('self_tasks') == 'on':
            author = getattr(self.request, 'user')
            return parent.filter(author=author)
        return parent

