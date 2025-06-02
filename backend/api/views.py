from rest_framework import viewsets

from .models import StampCard, StampEntry
from .serializers import StampCardSerializer, StampEntrySerializer

class StampCardViewSet(viewsets.ModelViewSet):
    queryset = StampCard.objects.filter(is_removed=False)
    serializer_class = StampCardSerializer

class StampEntryViewSet(viewsets.ModelViewSet):
    queryset = StampEntry.objects.all()
    serializer_class = StampEntrySerializer
