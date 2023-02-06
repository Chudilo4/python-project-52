import django_filters
from task_manager.models import Task


class TaskFilter(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'author']
