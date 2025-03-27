"""
Views for Dog APIs.
"""


from django.shortcuts import render
from .models import Breed, Dog
from .serializers import BreedSerializer, DogSerializer
from rest_framework import viewsets, mixins, status
from django.db.models import Prefetch


class BreedViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = BreedSerializer
    queryset = Breed.objects.all().prefetch_related(
        Prefetch('dog', queryset=Dog.objects.all().order_by('name'))
    )


class DogViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = DogSerializer
    queryset = Dog.objects.all().prefetch_related('breed')