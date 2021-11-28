from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'player1', 'player2', 'posted_on', 'winner')
    list_display_links = ('id', 'player1', 'player2', 'posted_on', 'winner')


admin.site.register(Room, RoomAdmin)
