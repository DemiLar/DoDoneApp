from django.urls import path

from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile_update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('get_token/', get_token, name='get_token'),
]

