from django.views.generic import TemplateView
from .models import Room


class StandbyView(TemplateView):
    template_name = 'rooms/standby.html'

    def get(self, request, *args, **kargs):
        Room.objects.create(player=request.user)
        return super().get(request, *args, **kargs)
