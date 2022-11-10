from django.contrib.auth.models import User
from django.db import models

from inventory.models import Item, Location


class Sale(models.Model):
    item = models.ForeignKey(Item, related_name='sales', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    location = models.ForeignKey(Location, related_name='sales', on_delete=models.PROTECT)
    status = models.IntegerField(default=1)
    creator = models.ForeignKey(User, related_name='sales', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    deleted_at = models.DateTimeField(null=True)
