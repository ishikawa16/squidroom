from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('list/', views.PlayerListView.as_view(), name='player_list'),
    path('detail/<int:pk>/', views.PlayerDetailView.as_view(), name='player_detail'),
]
