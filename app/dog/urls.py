"""
URL mappings for the dog app.
"""


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dog import views

router = DefaultRouter()
router.register('dogs', views.DogViewSet)
router.register('breeds', views.BreedViewSet)

app = 'dog'

urlpatterns = [
    path('', include(router.urls)),
]
