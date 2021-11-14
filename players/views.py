from django.views.generic import ListView, DetailView
from accounts.models import CustomUser


class PlayerListView(ListView):
    model = CustomUser
    template_name = 'players/player_list.html'
    context_object_name = 'player_list'


class PlayerDetailView(DetailView):
    model = CustomUser
    template_name = 'players/player_detail.html'
    context_object_name = 'player'
