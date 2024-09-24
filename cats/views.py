"""Cats views."""
from rest_framework import viewsets

from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Cats view."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    """Owners view."""

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
