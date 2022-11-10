from django.contrib.auth.models import User
from rest_framework import serializers
from sales.models import Sale


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sale
        fields = ['id', 'item', 'location', 'quantity', 'status', 'creator', 'created_at', 'updated_at', 'deleted_at']

