from django.urls import path
from .views import *


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('create_task/', TaskCreateView.as_view(), name='create_task'),
    path('task_update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete')

]
