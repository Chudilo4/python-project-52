from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Label(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Исполнитель', related_name='executors')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор', related_name='authors')
    created = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Label, through='Posrednk')

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ("author", "author"),
        )


class Posrednk(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    labels = models.ForeignKey(Label, on_delete=models.PROTECT)
