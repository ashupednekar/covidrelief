from django.db import models


class Centers(models.Model):
    center_name = models.TextField(null=True, blank=True)