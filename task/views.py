from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from task.models import Task, Worker

# Create your views here.
def home(request):
    return render(request, "task/home.html")


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task
    queryset = Task.objects.prefetch_related('assignees')

class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:task-list")
    template_name = "task/task_form.html"

class WorkerDetailView(generic.DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related('tasks')