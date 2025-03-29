"""
Views for Dog APIs.
"""


from .models import Breed, Dog
from . import serializers
from rest_framework import viewsets
from django.db.models import Prefetch, F, Avg, Count
from django.db.models.expressions import Window


class BreedViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.BreedDetailSerializer
    queryset = Breed.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.prefetch_related('dogs').only('id').annotate(
                dogs_count=Count('dogs')
                ).order_by('name')
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BreedSerializer
        return self.serializer_class


class DogViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.DogBaseSerializer
    queryset = Dog.objects.all()

    def get_queryset(self):
        if self.action == 'list':
            return self.queryset.annotate(
                avg_age=Window(
                    expression=Avg('age'), partition_by=[F('breed')]
                    )
                )
        return self.queryset.prefetch_related(
            Prefetch('breed')).annotate(dogs_count=Count('breed__dogs'))

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.DogSerializer
        if self.action == 'retrieve':
            return serializers.DogDetailSerializer
        return self.serializer_class
