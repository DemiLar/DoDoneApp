from rest_framework import routers
from todo_app_drf.views import MyTasksViewSet #MyProfileViewSet

my_task_router = routers.SimpleRouter()
my_task_router.register('', MyTasksViewSet, basename='my_tasks')

#my_profile_router = routers.SimpleRouter()
#my_profile_router.register('', MyProfileViewSet, basename='my_profile')

