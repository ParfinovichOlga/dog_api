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
    avg_age = serializers.SerializerMethodField()

    class Meta(DogBaseSerializer.Meta):
        fields = DogBaseSerializer.Meta.fields + ['avg_age']

    def get_avg_age(self, instance):
        return instance.avg_age


class DogDetailSerializer(DogBaseSerializer):
    """Serializer for retrieving dog."""
    dogs_count = serializers.SerializerMethodField()

    class Meta(DogBaseSerializer.Meta):
        fields = DogBaseSerializer.Meta.fields + ['dogs_count']

    def get_dogs_count(self, instance):
        return instance.dogs_count


class BreedDetailSerializer(serializers.ModelSerializer):
    """Serializer for retrieving breed."""

    class Meta:
        model = Breed
        fields = ['id', 'name', 'size', 'friendliness', 'trainability',
                  'shedding_amount', 'exercise_needs']
        read_only_fields = ['id']


class BreedSerializer(BreedDetailSerializer):
    """Serializer for breed list."""
    dogs_count = serializers.SerializerMethodField()

    class Meta(BreedDetailSerializer.Meta):
        fields = BreedDetailSerializer.Meta.fields + ['dogs_count']

    def get_dogs_count(self, instance):
        return instance.dogs_count
