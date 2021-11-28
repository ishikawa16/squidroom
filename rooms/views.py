from django.views.generic import TemplateView
from .models import Room


class BattleView(TemplateView):
    template_name = 'rooms/battle.html'

    def get_context_data(self, **kwargs):
        try:
            room = Room.objects.get(player1=self.request.user, winner=None)

        except Room.DoesNotExist:
            try:
                room = Room.objects.exclude(player1=self.request.user).filter(player2=None).earliest('posted_on')
                room.player2 = self.request.user
                room.save()
            except Room.DoesNotExist:
                room = Room.objects.create(player1=self.request.user)

        finally:
            context = super().get_context_data(**kwargs)
            context['room'] = room
            return context


class CancelView(TemplateView):
    template_name = 'rooms/cancel.html'

    def get(self, request, *args, **kargs):
        Room.objects.filter(player1=request.user).delete()
        return super().get(request, *args, **kargs)
