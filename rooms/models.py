from django.db import models
from accounts.models import CustomUser


class Room(models.Model):
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posted_time = models.DateTimeField(auto_now_add=True)
