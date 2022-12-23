"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.IndexView.as_view(), name='home'),
    path('users/', view.UsersView.as_view(), name='users'),
    path('users/create/', view.UsersCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', view.UsersUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', view.UsersDeleteView.as_view(), name='user_delete'),
    path('login/', view.LoginUserView.as_view(), name='login'),
    path('logout/', view.LogoutUserView.as_view(), name='logout'),
    path('statuses/', view.StatusesView.as_view(), name='statuses'),
    path('statuses/create/', view.StatusCreate.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', view.StatusUpdate.as_view(), name='status_udate'),
    path('statuses/<int:pk>/delete/', view.StatusDelete.as_view(), name='status_delete'),
    path('tasks/', view.TaskView.as_view(), name='task'),
    path('tasks/create/', view.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/update/', view.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', view.TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/', view.TaskShowView.as_view(), name='get_task'),
    path('labels/', view.LabelsView.as_view(), name='labels'),
    path('labels/create/', view.LabelCreateView.as_view(), name='label_create'),
    path('labels/<int:pk>/update/', view.LabelUpdateView.as_view(), name='label_update'),
    path('labels/<int:pk>/delete/', view.LabelDeleteView.as_view(), name='label_delete')
]
