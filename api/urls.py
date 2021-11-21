from api import views
from django.urls import path

urlpatterns = [
    path("", views.api_root),
    path("lists/", views.TodolistListCreateView.as_view(), name="todolist-list"),
    path("lists/<int:pk>/", views.TodolistDetailView.as_view(), name="todolist-detail"),
    path(
        "lists/<int:pk>/items/",
        views.TodoitemsOnListView.as_view(),
        name="todolist-items",
    ),
    path(
        "lists/<int:pk>/items/completed/",
        views.CompletedTodoitemsOnListView.as_view(),
        name="todolist-completed-items",
    ),
    path("items/", views.TodoitemsListView.as_view(), name="todoitem-list"),
    path("items/<int:pk>/", views.TodoItemDetailView.as_view(), name="todoitem-detail"),
    path(
        "items/<int:pk>/complete",
        views.CompleteTodoItemView.as_view(),
        name="todoitem-complete",
    ),
]
