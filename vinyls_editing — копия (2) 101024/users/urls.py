from django.urls import path
from .views import (
UserProfileView, RegisterView, UserLoginView,
UserLogoutView, UserPasswordChangeView
)
app_name = 'users'
urlpatterns = [
path('profile/', UserProfileView.as_view(), name='profile'),
path('register/', RegisterView.as_view(), name='register'),
path('login/', UserLoginView.as_view(), name='login'),
path('logout/', UserLogoutView.as_view(), name='logout'),
path('password-change/', UserPasswordChangeView.as_view(), name='password_change'),
]