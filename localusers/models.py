from django.contrib.auth.models import AbstractUser
from django.db import models


class LocalUser(AbstractUser, models.Model):
    # USERNAME_FIELD = 'card_no'
    full_name = models.CharField(max_length=500, blank=True, null=True)
    account_no = models.CharField(max_length=500, blank=True, null=True)
    card_no = models.CharField(max_length=500, blank=True, null=True, unique=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    disabled = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateField(auto_now=True)