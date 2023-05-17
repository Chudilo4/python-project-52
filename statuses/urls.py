from django.urls import path, include
from user.view import HomeView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, Login

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('statuses/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]