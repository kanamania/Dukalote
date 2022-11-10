from rest_framework import serializers
from inventory.models import *
from settings.serializers import UserSerializer


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    def get_modifier_name(self, obj):
        try:
            modifier = User.objects.filter(pk=obj.modifier).first()
            return modifier.first_name + ' ' + modifier.last_name
        except:
            return ''

    class Meta:
        model = Item
        fields = ['id', 'name', 'image', 'creator_name', 'created_at', 'modifier_name', 'updated_at', 'deleted_at']


class ItemPriceSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name


    class Meta:
        model = ItemPrice
        fields = ['id', 'item', 'location', 'price', 'creator_name', 'created_at']


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    def get_modifier_name(self, obj):
        try:
            modifier = User.objects.filter(pk=obj.modifier).first()
            return modifier.first_name + ' ' + modifier.last_name
        except:
            return ''

    class Meta:
        model = Location
        fields = ['id', 'address', 'name', 'creator_name', 'modifier_name', 'created_at', 'updated_at', 'deleted_at']


class StockSerializer(serializers.HyperlinkedModelSerializer):
    available = serializers.SerializerMethodField()
    unavailable = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    def get_available(self, obj):  # TODO get available stock at location/item
        return 0

    def get_unavailable(self, obj):  # TODO get unavailable stock at location/item
        return 0

    def get_total(self, obj):  # TODO get total stock at location/item
        return 0

    class Meta:
        model = Stock
        fields = ['id', 'location', 'item', 'total', 'available', 'unavailable', 'creator_name', 'modifier_name', 'created_at',
                  'deleted_at']


class StockLogSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    class Meta:
        model = StockLog
        fields = ['id', 'location', 'item', 'quantity', 'creator_name', 'created_at']
