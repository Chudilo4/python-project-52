import django_filters

from .models import Task, Label


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelMultipleChoiceFilter(label='Метка',
                                                      queryset=Label.objects.all(),
                                                      conjoined=True)

    class Meta:
        model = Task
        fields = ['status', 'labels', 'executor']

    @property
    def qs(self):
        parent = super().qs
        if self.request.GET.get('self_tasks') == 'on':
            author = getattr(self.request, 'user')
            return parent.filter(author=author)
        return parent
