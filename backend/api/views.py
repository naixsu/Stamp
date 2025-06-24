from rest_framework import viewsets, filters

from .models import StampCard, StampEntry
from .serializers import StampCardSerializer, StampEntrySerializer

class StampCardViewSet(viewsets.ModelViewSet):
    queryset = StampCard.objects.filter(is_removed=False)
    serializer_class = StampCardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class StampEntryViewSet(viewsets.ModelViewSet):
    queryset = StampEntry.objects.all()
    serializer_class = StampEntrySerializer
