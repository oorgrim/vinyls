from django.urls import path
from .views import CreateVinylView, CreateTagView, VinylDetailView, VinylListView

app_name = 'vinyls'

urlpatterns = [
path('vinyls/', VinylListView.as_view(), name='vinyl_list'),
path('vinyls/add/', CreateVinylView.as_view(), name='vinyl_add'),
path('vinyls/detail/<int:pk>/', VinylDetailView.as_view(), name='vinyl_detail'),
path('tags/add/', CreateTagView.as_view(), name='tag_add'),
]