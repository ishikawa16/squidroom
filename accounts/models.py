from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    rate = models.IntegerField(default=1500, verbose_name='rate')
    code = models.CharField(help_text='Fill in as "xxxx-xxxx-xxxx."', max_length=20, validators=[RegexValidator(r'^\d{4}-\d{4}-\d{4}$', 'Your code was inappropriate.')], verbose_name='friend code')
