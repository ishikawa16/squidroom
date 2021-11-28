from django.db import models
from accounts.models import CustomUser


class Room(models.Model):
    player1 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player1', verbose_name='player1')
    player2 = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='player2', verbose_name='player2', blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True, verbose_name='posted_on')
    result = models.IntegerField(default=0, verbose_name='result')
