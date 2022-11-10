from rest_framework import serializers
from inventory.models import *


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'image', 'creator', 'created_at', 'modifier', 'updated_at', 'deleted_at']


class ItemPriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ItemPrice
        fields = ['id', 'item', 'location', 'price', 'creator', 'created_at']


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'address', 'name', 'creator', 'modifier', 'created_at', 'updated_at', 'deleted_at']


class StockSerializer(serializers.HyperlinkedModelSerializer):
    available = serializers.SerializerMethodField()
    unavailable = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = ['id', 'location', 'item', 'total', 'available', 'unavailable', 'creator', 'modifier', 'created_at',
                  'deleted_at']

    def get_available(self, obj):  # TODO get available stock at location/item
        return 0

    def get_unavailable(self, obj):  # TODO get unavailable stock at location/item
        return 0

    def get_total(self, obj):  # TODO get total stock at location/item
        return 0


class StockLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockLog
        fields = ['id', 'location', 'item', 'quantity', 'creator', 'created_at']
