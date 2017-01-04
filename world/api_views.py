from rest_framework import viewsets
from .models import RegionBorder, AustriaBorders, WorldBorder
from .serializers import RegionBorderSerializer, AustriaBordersSerializer, WorldBorderSerializer


class RegionBorderViewSet(viewsets.ModelViewSet):

    queryset = RegionBorder.objects.all()
    serializer_class = RegionBorderSerializer


class AustriaBordersViewSet(viewsets.ModelViewSet):

    queryset = AustriaBorders.objects.all()
    serializer_class = AustriaBordersSerializer


class WorldBorderViewSet(viewsets.ModelViewSet):

    queryset = WorldBorder.objects.all()
    serializer_class = WorldBorderSerializer
