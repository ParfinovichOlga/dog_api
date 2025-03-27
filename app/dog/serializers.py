"""
Serializer for dogs.
"""

from rest_framework import serializers
from .models import Breed, Dog


class DogSerializer(serializers.ModelSerializer):
    """Serializer for dogs."""
    breed = serializers.CharField(source='breed.name')
    class Meta:
        model = Dog
        fields = ('__all__')
        read_only_fields = ['id']


class BreedSerializer(serializers.ModelSerializer):
    """Serializer for breeds."""
    dogs = DogSerializer(many=True, required=False)
    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability',
                  'shedding_amount', 'exercise_needs', 'dogs']
        read_only_fields = ['id']
