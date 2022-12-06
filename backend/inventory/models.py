from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    creator = models.ForeignKey(User, related_name='created_items', on_delete=models.PROTECT)
    modifier = models.ForeignKey(User, related_name='modified_items', null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    creator = models.ForeignKey(User, related_name='created_locations', on_delete=models.PROTECT)
    modifier = models.ForeignKey(User, related_name='modified_locations', null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class ItemPrice(models.Model):
    location = models.ForeignKey(Location, related_name='item_prices', on_delete=models.PROTECT)
    item = models.ForeignKey(Item, related_name='item_prices', on_delete=models.PROTECT)
    price = models.BigIntegerField()
    creator = models.ForeignKey(User, related_name='created_item_prices', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)


class Stock(models.Model):
    location = models.ForeignKey(Location, related_name='stocks', on_delete=models.PROTECT)
    item = models.ForeignKey(Item, related_name='stocks', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    creator = models.ForeignKey(User, related_name='created_stocks', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)


class StockLog(models.Model):
    location = models.ForeignKey(Location, related_name='stock_logs', on_delete=models.PROTECT)
    item = models.ForeignKey(Item, related_name='stock_logs', on_delete=models.PROTECT)
    quantity = models.IntegerField()
    creator = models.ForeignKey(User, related_name='created_stock_logs', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
