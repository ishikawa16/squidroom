from django.views.generic import TemplateView
from .models import Room


class BattleView(TemplateView):
    template_name = 'rooms/battle.html'

    def get(self, request, *args, **kargs):
        Room.objects.create(player=request.user)
        return super().get(request, *args, **kargs)


class CancelView(TemplateView):
    template_name = 'rooms/cancel.html'

    def get(self, request, *args, **kargs):
        Room.objects.filter(player=request.user).delete()
        return super().get(request, *args, **kargs)
