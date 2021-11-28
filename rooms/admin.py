from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'player1', 'player2', 'winner', 'posted_on')
    list_display_links = ('id',)


admin.site.register(Room, RoomAdmin)
