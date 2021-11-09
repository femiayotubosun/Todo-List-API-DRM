from django.forms import fields
from rest_framework import serializers
from rest_framework.fields import IntegerField, ListField
from api.models import TodoItem, TodoList


class TodoItemSingleSerializer(serializers.ModelSerializer):
    todo_list = serializers.ReadOnlyField(source="todo_list.name")
    todo_list_id = serializers.ReadOnlyField(source="todo_list.id")

    class Meta:
        model = TodoItem
        fields = [
            "id",
            "detail",
            "date_added",
            "todo_list",
            "todo_list_id",
            "completed",
            "date_completed",
        ]


class TodoItemsOnListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = [
            "id",
            "detail",
            "completed",
            "date_added",
            "date_completed",
        ]


class TodoItemCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ["id"]
        read_only_fields = ["id", "detail", "completed", "date_added", "date_completed"]


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = [
            "id",
            "name",
        ]
