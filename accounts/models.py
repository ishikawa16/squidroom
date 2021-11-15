from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    rate = models.IntegerField(default=1500, verbose_name='rate')
