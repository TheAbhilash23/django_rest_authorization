from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_2 import models


class MovieGenreSerializer(ModelSerializer):

    class Meta:
        model = models.MovieGenre
        fields = (
            'id',
            'name',
            'description',
            'release_year',
            'rating',
            'is_available',
            
        )


class RestaurantMenuSerializer(ModelSerializer):

    class Meta:
        model = models.RestaurantMenu
        fields = (
            'id',
            'name',
            'category',
            'price',
            'is_vegetarian',
            'preparation_time',
            
        )


