from django.contrib.auth.models import User
from django.db import models

from inventory.models import Item, Location


class Sale(models.Model):
    item = models.ForeignKey(Item, related_name='sales')
    quantity = models.IntegerField(default=1)
    location = models.ForeignKey(Location, related_name='sales')
    status = models.IntegerField(default=1)
    creator = models.ForeignKey(User, related_name='sales')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)
