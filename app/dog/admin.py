from django.contrib import admin
from .models import Dog, Breed


class DogAdmin(admin.ModelAdmin):
    """Define the dog page for users."""
    list_filter = ('breed', 'gender', 'color')


class BreedAdmin(admin.ModelAdmin):
    """Define the dog page for users."""
    list_filter = (
        'name', 'size', 'friendliness',
        'trainability', 'shedding_amount',
        'exercise_needs'
    )


admin.site.register(Breed, BreedAdmin)
admin.site.register(Dog, DogAdmin)
