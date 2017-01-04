from rest_framework import viewsets
from .models import RegionBorder
from .serializers import RegionBorderSerializer


class RegionBorderViewSet(viewsets.ModelViewSet):

    queryset = RegionBorder.objects.all()
    serializer_class = RegionBorderSerializer
