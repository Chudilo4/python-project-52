import django_filters

from django import forms
from .models import Task, Label


class TaskFilter(django_filters.FilterSet):
    label = django_filters.ModelMultipleChoiceFilter(label='Метка',
                                                     queryset=Label.objects.all(),
                                                     conjoined=True)

    class Meta:
        model = Task
        fields = ['status', 'label', 'executor']

    @property
    def qs(self):
        parent = super().qs
        if self.request.GET.get('self_tasks') == 'on':
            author = getattr(self.request, 'user')
            return parent.filter(author=author)
        return parent
