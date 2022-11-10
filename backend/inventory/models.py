from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    creator = models.ForeignKey(User, related_name='items')
    modifier = models.ForeignKey(User, related_name='items', null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    creator = models.ForeignKey(User, related_name='locations')
    modifier = models.ForeignKey(User, related_name='locations', null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class ItemPrice(models.Model):
    location = models.ForeignKey(Location, related_name='stock_logs')
    item = models.ForeignKey(Item, related_name='stock_logs')
    price = models.BigIntegerField()
    creator = models.ForeignKey(User, related_name='item_prices')
    created_at = models.DateTimeField()


class Stock(models.Model):
    location = models.ForeignKey(Location, related_name='stocks')
    item = models.ForeignKey(Item, related_name='stocks')
    quantity = models.IntegerField()
    creator = models.ForeignKey(User, related_name='stocks')
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(null=True)


class StockLog(models.Model):
    location = models.ForeignKey(Location, related_name='stock_logs')
    item = models.ForeignKey(Item, related_name='stock_logs')
    quantity = models.IntegerField()
    creator = models.ForeignKey(User, related_name='stock_logs')
    created_at = models.DateTimeField()
