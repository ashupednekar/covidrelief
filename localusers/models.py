from django.contrib.auth.models import AbstractUser
from django.db import models


class LocalUser(AbstractUser, models.Model):
    # USERNAME_FIELD = 'card_no'
    full_name = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    disabled = models.CharField(max_length=500, blank=True, null=True)
    center = models.CharField(max_length=500, blank=True, null=True, default='unassigned')
    timestamp = models.DateField(auto_now=True)
