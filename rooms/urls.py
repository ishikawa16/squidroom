from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('standby/', views.StandbyView.as_view(), name='standby'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
]
