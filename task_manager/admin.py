from django.contrib import admin

from task_manager.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
