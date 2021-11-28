from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .models import Room


def calculate_rate(ri, rj):
    d = ri - rj
    e = 1 / (1 + 10 ** (-d / 400))
    new_ri = ri + 32 * (1 - e)
    new_rj = rj + 32 * (e - 1)
    return new_ri, new_rj


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

    def post(self, request, *args, **kargs):
        room = Room.objects.get(Q(player1=self.request.user) | Q(player2=self.request.user), winner=None)
        p1, p2 = room.player1, room.player2
        r1, r2 = p1.rate, p2.rate

        if 'player1' in request.POST:
            new_r1, new_r2 = calculate_rate(r1, r2)
            p1.rate = new_r1
            p1.save()
            p2.rate = new_r2
            p2.save()
            room.winner = room.player1
            room.save()

        if 'player2' in request.POST:
            new_r2, new_r1 = calculate_rate(r2, r1)
            p1.rate = new_r1
            p1.save()
            p2.rate = new_r2
            p2.save()
            room.winner = room.player2
            room.save()

        return redirect('/')


class CancelView(TemplateView):
    template_name = 'rooms/cancel.html'

    def get(self, request, *args, **kargs):
        Room.objects.filter(player1=request.user).delete()
        return super().get(request, *args, **kargs)
