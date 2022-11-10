from datetime import datetime

from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from settings.permissions import IsOwnerOrReadOnly
from settings.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = SettingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.modifier = self.request.user
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.exclude(deleted_at__isnull=True).all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.modifier = self.request.user
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.modifier = self.request.user
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)

    def destroy(self, request, *args, **kwargs):
        model = self.get_object()
        model.modifier = self.request.user
        model.deleted_at = datetime.now()
        model.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
