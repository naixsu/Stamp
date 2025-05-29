from rest_framework import viewsets, filters

from .models import StampCard
from .serializers import StampCardSerializer

class StampCardViewSet(viewsets.ModelViewSet):
    queryset = StampCard.objects.filter(is_removed=False)
    serializer_class = StampCardSerializer
