from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics


from .models import StampCard
from .serializers import StampCardSerializer

@api_view(['GET'])
def hello(request):
    return Response({"message": "Hello from Django backend!"})

class ActiveStampCardListView(generics.ListAPIView):
    queryset = StampCard.objects.filter(is_removed=False)
    serializer_class = StampCardSerializer
