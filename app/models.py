from django.db import models


class Centers(models.Model):
    center_name = models.TextField(null=True, blank=True)


class Entries(models.Model):
    name = models.TextField(null=True, blank=True)
    mobile = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    landmark = models.TextField(null=True, blank=True)
    center = models.TextField(null=True, blank=True)
    remark = models.TextField(null=True, blank=True)
    closed = models.CharField(max_length=10, default='N')
    image = models.URLField(null=True, blank=True)
    date_received = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_closed = models.DateTimeField(auto_now=True, null=True, blank=True)
