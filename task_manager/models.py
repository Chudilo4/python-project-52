from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    data_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
