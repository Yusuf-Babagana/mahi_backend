from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserProfileView, debug_register

urlpatterns = [
    path('debug-register/', debug_register),  # Temporary debug
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('me/', UserProfileView.as_view(), name='profile'),
]