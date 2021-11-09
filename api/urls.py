from django.urls import path
from api.views import (
    CompleteTodoItemView,
    CompletedTodoitemsOnListView,
    TodoItemDetailView,
    TodoitemsListView,
    TodoitemsOnListView,
    api_root,
    TodolistListCreateView,
    TodolistDetailView,
)

urlpatterns = [
    path("", api_root),
    path("lists/", TodolistListCreateView.as_view(), name="todolist-list"),
    path("lists/<int:pk>/", TodolistDetailView.as_view(), name="todolist-detail"),
    path(
        "lists/<int:pk>/items/",
        TodoitemsOnListView.as_view(),
        name="todolist-items",
    ),
    path(
        "lists/<int:pk>/items/completed/",
        CompletedTodoitemsOnListView.as_view(),
        name="todolist-completed-items",
    ),
    path("items/", TodoitemsListView.as_view(), name="todoitem-list"),
    path("items/<int:pk>/", TodoItemDetailView.as_view(), name="todoitem-detail"),
    path(
        "items/<int:pk>/complete",
        CompleteTodoItemView.as_view(),
        name="todoitem-complete",
    ),
]
