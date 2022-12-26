from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(max_length=700,
                                   verbose_name='Description')
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               verbose_name='Status')
    creator = models.ForeignKey(User,
                                on_delete=models.PROTECT,
                                related_name='creator')
    executor = models.ForeignKey(User, on_delete=models.PROTECT,
                                 null=True,
                                 verbose_name='Executor')
    created_at = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Label,
                                    verbose_name='Labels')

    def __str__(self):
        return self.name

