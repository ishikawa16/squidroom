from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'rate', 'code')
    list_display_links = ('id', 'username', 'rate', 'code')


admin.site.register(CustomUser, CustomUserAdmin)
