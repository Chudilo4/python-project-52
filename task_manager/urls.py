"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from task_manager.models import Task
from task_manager.views import (
    HomeView, UserListView,
    UserCreateView, UserUpdateView,
    UserDeleteView, Login, Logout, StatusListView,
    StatusCreateView, StatusUpdateView,
    StatusDeleteView, TaskListView,
    TaskCreateView, TaskUpdateView,
    TaskDeleteView, TaskDetailView,
    LabelListView, LabelCreateView,
    LabelDeleteView, LabelUpdateView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('statuses/', StatusListView.as_view(), name="status_list"),
    path('statuses/create/', StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('tasks/', TaskListView.as_view(model=Task), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('labels/', LabelListView.as_view(), name='label_list'),
    path('labels/create/', LabelCreateView.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),

]
