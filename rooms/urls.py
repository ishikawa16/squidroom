from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('battle/', views.BattleView.as_view(), name='battle'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
]
