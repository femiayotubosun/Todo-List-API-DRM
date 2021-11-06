from unittest import skip
from django.test import TestCase
from django.db import IntegrityError
from api.models import TodoList, TodoItem


class TodoListTest(TestCase):
    def test_create_todo_list_should_add_to_database_correctly(self):
        count: int = TodoList.objects.all().count()
        list: TodoList = TodoList.objects.create(name="Test List")
        expected: str = "Test List"
        self.assertEqual(list.__str__(), expected)
        self.assertEqual(count + 1, TodoList.objects.all().count())


class TodoItemTest(TestCase):
    def setUp(self):
        self.test_list: TodoList = TodoList.objects.create(name="Test Todo-list")

    def test_create_todo_item_invalid_data_should_return_exception(self):
        with self.assertRaises(Exception) as context:
            item: TodoItem = TodoItem.objects.create(detail="Test detail")
        self.assertTrue(isinstance(context.exception, IntegrityError))

    def test_create_todo_item_with_valid_data_should_add_to_db_correctly(self):
        count: int = TodoItem.objects.all().count()
        item: TodoItem = TodoItem.objects.create(
            detail="Test detail", todo_list=self.test_list
        )
        expected = "Test detail from Test Todo-list (incomplete)"
        self.assertEqual(count + 1, TodoItem.objects.all().count())
        self.assertEqual(expected, item.__str__())
