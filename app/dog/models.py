"""
Database models.
"""


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    """Breed object."""
    size_range = (
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large')
    )
    valid_values = [MinValueValidator(1), MaxValueValidator(5)]
    name = models.CharField(max_length=100)
    size = models.CharField(choices=size_range, max_length=8)
    friendliness = models.IntegerField(validators=valid_values)
    trainability = models.IntegerField(validators=valid_values)
    shedding_amount = models.IntegerField(validators=valid_values)
    exercise_needs = models.IntegerField(validators=valid_values)

    def __str__(self):
        return self.name


class Dog(models.Model):
    """Dog object."""
    genders = (('male', 'Male'), ('female', 'Female'))
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    breed = models.ForeignKey(
        Breed, on_delete=models.CASCADE, related_name='dogs'
        )
    gender = models.CharField(choices=genders, max_length=6)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=200)
    favorite_toy = models.CharField(max_length=200)

    def __str__(self):
        return self.name
