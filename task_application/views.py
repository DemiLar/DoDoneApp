from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Avg, F

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import Task


class MainPageView(TemplateView):
    template_name = 'task_application/main_page.html'


def task_list(request):
    task = Task.objects.filter(user_id=request.user)
    paginator = Paginator(task, 3)
    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)
    return render(request,
                  'task_application/task_list.html',
                  {'page': page,
                   'tasks': tasks})


def statistic_list(request):
    num_tasks = Task.objects.filter(user_id=request.user).count()
    num_tasks_todo = Task.objects.filter(user_id=request.user, status='ToDo').count()
    num_tasks_in_progress = Task.objects.filter(user_id=request.user, status='In_progress').count()
    num_tasks_blocked = Task.objects.filter(user_id=request.user, status='Blocked').count()
    num_tasks_finished = Task.objects.filter(user_id=request.user, status='Finished').count()
    average_duration = Task.objects.aggregate(avg_time=Avg(F('done_date') - F('created')))
    return render(request,
                  'task_application/statistic_list.html',
                  {'num_tasks': num_tasks,
                   'num_tasks_todo': num_tasks_todo,
                   'num_tasks_in_progress': num_tasks_in_progress,
                   'num_tasks_blocked': num_tasks_blocked,
                   'num_tasks_finished': num_tasks_finished,
                   'average_duration': average_duration}
                  )


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
