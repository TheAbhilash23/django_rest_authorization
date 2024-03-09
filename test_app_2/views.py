from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_2 import models
from test_app_2 import serializers


class MovieGenreView(ModelSerializer):
    queryset = models.MovieGenre.objects.all()
    serializer_class = serializers.MovieGenreSerializer


class RestaurantMenuView(ModelSerializer):
    queryset = models.RestaurantMenu.objects.all()
    serializer_class = serializers.RestaurantMenuSerializer


