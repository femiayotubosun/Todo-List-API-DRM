from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    UpdateAPIView,
)
from api.models import TodoItem, TodoList
from api.serializers import (
    TodoItemCompleteSerializer,
    TodoItemSingleSerializer,
    TodoItemsOnListSerializer,
    TodoListSerializer,
)

# Create your views here.


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "todolists": reverse("todolist-list", request=request, format=None),
            "todoitems": reverse("todoitem-list", request=request, format=None),
        }
    )


class TodolistListCreateView(ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodolistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


# How to get url params
class TodoitemsOnListView(ListCreateAPIView):
    serializer_class = TodoItemsOnListSerializer

    def get_queryset(self):
        todo_list = TodoList.objects.get(pk=self.kwargs["pk"])
        return TodoItem.objects.filter(todo_list=todo_list)

    def perform_create(self, serializer):
        todo_list = TodoList.objects.get(pk=self.kwargs["pk"])
        serializer.save(todo_list=todo_list)
        # item = TodoItem.objects.create(todo_list=todo_list, **serializer.data)

        # return TodoItemsOnListSerializer(item)


class TodoitemsListView(ListAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSingleSerializer


class TodoItemDetailView(RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSingleSerializer

    def perform_update(self, serializer):
        if "todo_list_id" in serializer.validated_data:
            todo_list = TodoList.objects.get(
                pk=serializer.validated_data["todo_list_id"]
            )
            serializer.save(
                todo_list=todo_list,
            )
        instance = serializer.save()


class CompleteTodoItemView(UpdateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemCompleteSerializer

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.instance.completed = True
        serializer.save()
