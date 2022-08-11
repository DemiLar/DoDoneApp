from rest_framework import routers
from account_drf.views import MyProfileViewSet


my_profile_router = routers.SimpleRouter()
my_profile_router.register('', MyProfileViewSet, basename='my_profile')