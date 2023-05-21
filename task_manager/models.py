from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(blank=False, null=False,
                            verbose_name='Имя', max_length=255)
    created_time = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name='Дата обновления')

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(blank=False, null=False, verbose_name='Имя', max_length=255)
    description = models.TextField(verbose_name='Описание')
    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 verbose_name='Исполнитель', related_name='task_exectot')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус',
                               related_name='task_status')
    label = models.ManyToManyField("Label", through='LabelsOfTask', verbose_name='Метки')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор',
                               related_name='task_author')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(blank=False, null=False, verbose_name='Имя', max_length=255)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name


class LabelsOfTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
