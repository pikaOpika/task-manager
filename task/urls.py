from django.contrib import admin
from django.urls import path
from task.views import (
    home,
    TaskListView,
    TaskDetailView,
    WorkerDetailView,
    TaskCreateView,
)


urlpatterns = [
    path("", home, name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("workplace/<int:pk>", WorkerDetailView.as_view(), name="worker-detail")

]

app_name = "task"
