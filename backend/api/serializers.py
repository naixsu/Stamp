from rest_framework import serializers
from .models import StampCard

class StampCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StampCard
        fields = [
            'pk',
            'title',
            'stamps_needed',
            'stamps_collected',
            'is_redeemed',
            'date_created',
        ]
