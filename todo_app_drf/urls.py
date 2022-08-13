from rest_framework import routers
from todo_app_drf.views import MyTasksViewSet

my_task_router = routers.SimpleRouter()
my_task_router.register('', MyTasksViewSet, basename='my_tasks')


