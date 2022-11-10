from datetime import datetime

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from inventory.permissions import IsOwnerOrReadOnly
from inventory.serializers import *


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ItemPriceViewSet(viewsets.ModelViewSet):
    queryset = ItemPrice.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = ItemPriceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
