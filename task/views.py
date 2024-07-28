from django.shortcuts import render
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

class WorkerDetailView(generic.DetailView):
    model = Worker