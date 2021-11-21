from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'posted_time')
    list_display_links = ('id', 'player', 'posted_time')


admin.site.register(Room, RoomAdmin)
