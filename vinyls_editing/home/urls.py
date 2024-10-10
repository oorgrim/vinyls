from django.urls import path
from .views import HomePageView
app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('', include(('home.urls', 'home'), namespace='home')),

]
