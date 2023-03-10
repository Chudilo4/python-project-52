# Generated by Django 4.1.6 on 2023-02-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('author', 'author'),)},
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(to='task_manager.label'),
        ),
    ]
