from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    detail = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self) -> str:
        return f"{self.detail} from {self.todo_list.__str__()} {'(complete)' if self.completed else '(incomplete)'}"
