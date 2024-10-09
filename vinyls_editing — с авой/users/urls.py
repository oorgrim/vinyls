from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
