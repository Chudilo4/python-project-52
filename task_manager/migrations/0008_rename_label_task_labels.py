# Generated by Django 4.2.1 on 2023-05-21 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0007_alter_task_executor_alter_task_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='label',
            new_name='labels',
        ),
    ]
