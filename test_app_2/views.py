from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_2 import models
from test_app_2 import serializers


class MovieGenreView(ModelViewSet):
    queryset = models.MovieGenre.objects.all()
    serializer_class = serializers.MovieGenreSerializer


class RestaurantMenuView(ModelViewSet):
    queryset = models.RestaurantMenu.objects.all()
    serializer_class = serializers.RestaurantMenuSerializer


