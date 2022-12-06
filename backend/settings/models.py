from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    creator = models.ForeignKey(User, related_name='created_categories', on_delete=models.PROTECT)
    modifier = models.ForeignKey(User, related_name='modified_categories', null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Region(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, related_name='created_regions', on_delete=models.PROTECT)
    modifier = models.ForeignKey(User, related_name='modified_regions', null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class District(models.Model):
    name = models.CharField(max_length=200)
    region = models.BigIntegerField()
    creator = models.ForeignKey(User, related_name='created_districts', on_delete=models.PROTECT)
    modifier = models.ForeignKey(User, related_name='modified_districts', null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


class Log(models.Model):
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    old = models.TextField(null=True)
    new = models.TextField(null=True)
    record = models.BigIntegerField()
    creator = models.ForeignKey(User, related_name='created_logs', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField()


class Setting(models.Model):
    tag = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    default_value = models.TextField(null=True)
    current_value = models.TextField(null=True)
    category = models.CharField(max_length=32)
    creator = models.ForeignKey(User, related_name='created_settings', on_delete=models.PROTECT)
    modifier = models.ForeignKey(User, related_name='modified_settings', null=True, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)


