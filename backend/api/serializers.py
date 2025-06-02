from rest_framework import serializers
from .models import (
    StampCard,
    StampEntry,
)


class StampEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StampEntry
        fields = ['pk', 'is_active', 'notes', 'date_created']

class StampCardSerializer(serializers.ModelSerializer):
    entries = StampEntrySerializer(many=True, read_only=True)

    class Meta:
        model = StampCard
        fields = [
            'pk',
            'title',
            'stamps_needed',
            'stamps_collected',
            'is_redeemed',
            'is_removed',
            'date_created',
            'entries',
        ]

    def create(self, validated_data):
        stamps_needed = validated_data.get('stamps_needed', 10) # Default for `stamps_needed`
        stamp_card = StampCard.objects.create(**validated_data)

        # Bulk create StampEntry objects
        StampEntry.objects.bulk_create([
            StampEntry(stamp_card=stamp_card) for _ in range(stamps_needed)
        ])

        return stamp_card
