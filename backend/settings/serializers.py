from django.contrib.auth.models import User
from rest_framework import serializers
from settings.models import District, Region, Category, Log, Setting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'url', 'name', 'first_name', 'last_name', 'username', 'email', 'groups']

    def get_name(self, obj):
        return obj.first_name + ' ' + obj.last_name


class CategorySerializer(serializers.HyperlinkedModelSerializer):
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
        model = Category
        fields = ['id', 'description', 'name', 'creator_name', 'modifier_name', 'created_at', 'updated_at']


class RegionSerializer(serializers.HyperlinkedModelSerializer):
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
        model = Region
        fields = ['id', 'name', 'creator_name', 'modifier_name', 'created_at', 'updated_at']


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()
    modifier_name = serializers.SerializerMethodField()
    region_name = serializers.SerializerMethodField()

    def get_region_name(self, obj):
        return Region.objects.filter(pk=obj.region).first().name

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    def get_modifier_name(self, obj):
        try:
            modifier = User.objects.filter(pk=obj.modifier).first()
            return modifier.first_name + ' ' + modifier.last_name
        except:
            return ''

    class Meta:
        model = District
        fields = ['id', 'region_name', 'name', 'creator_name', 'modifier_name', 'created_at', 'updated_at']


class LogSerializer(serializers.HyperlinkedModelSerializer):
    creator_name = serializers.SerializerMethodField()

    def get_creator_name(self, obj):
        return UserSerializer(obj.creator).name

    class Meta:
        model = Log
        fields = ['id', 'tag', 'description', 'old', 'new', 'record' 'creator_name', 'created_at']


class SettingSerializer(serializers.HyperlinkedModelSerializer):
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
        model = Setting
        fields = ['id', 'tag', 'description', 'default_value', 'current_value', 'category' 'creator_name', 'modifier_name',
                  'created_at', 'updated_at']
