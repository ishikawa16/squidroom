from django.contrib import admin
from .models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'posted_on')
    list_display_links = ('id', 'player', 'posted_on')


admin.site.register(Room, RoomAdmin)
