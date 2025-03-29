"""
Serializer for dogs.
"""

from rest_framework import serializers
from .models import Breed, Dog


class DogBaseSerializer(serializers.ModelSerializer):
    """Base Serializer for dogs."""

    class Meta:
        model = Dog
        fields = [
            'id', 'name', 'age', 'breed', 'gender', 'color',
            'favorite_food', 'favorite_toy'
            ]
        read_only_fields = ['id']


class DogSerializer(DogBaseSerializer):
    """Serializer for dogs list."""
    avg_age = serializers.IntegerField(read_only=True)

    class Meta(DogBaseSerializer.Meta):
        fields = DogBaseSerializer.Meta.fields + ['avg_age']


class DogDetailSerializer(DogBaseSerializer):
    """Serializer for retrieving dog."""
    dogs_count = serializers.IntegerField(read_only=True)

    class Meta(DogBaseSerializer.Meta):
        fields = DogBaseSerializer.Meta.fields + ['dogs_count']


class BreedSerializer(serializers.ModelSerializer):
    """Serializer for retrieving breed."""
    dogs_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability',
                  'shedding_amount', 'exercise_needs', 'dogs_count']
        read_only_fields = ['id']
