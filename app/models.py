import uuid

from django.db import models


class Centers(models.Model):
    center_name = models.TextField(null=True, blank=True)
    stock_count = models.IntegerField(null=True, blank=True, default=0)


class Entries(models.Model):
    actor = models.TextField(null=True, blank=True)
    ward = models.TextField(null=True, blank=True)
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


class Upload(models.Model):
    tomark = models.TextField(null=True, blank=True)
    fn = models.FileField(null=True, blank=True)


class Stocks(models.Model):
    count = models.IntegerField(null=True, blank=True, default=0)


class Shipments(models.Model):
    shipment_id = models.TextField(null=True, blank=True, default=str(uuid.uuid4()))
    sender = models.TextField(null=True, blank=True)
    center = models.TextField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    delivered = models.TextField(null=True, blank=True, default='N')  # delivered to center
