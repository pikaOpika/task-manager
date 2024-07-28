from django.db import models
from django.contrib.auth.models import AbstractUser

class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    deadline = models.DateField()
    is_completed = models.BooleanField()
    priority = models.CharField(
        max_length=1,
        choices=[
            ("U", "Urgent"),
            ("H", "High"),
            ('M', 'Medium'),
            ('L', 'Low'),
        ],
        default="M",
    )
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    assignees = models.ManyToManyField(
        Worker,
        related_name="tasks"
    )

    def __str__(self) -> str:
        return f"{self.task_type} {self.get_priority_display()} priority"
