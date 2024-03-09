from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_1 import models


class BookCategorySerializer(ModelSerializer):

    class Meta:
        model = models.BookCategory
        fields = (
            'id',
            'name',
            'description',
            'publication_year',
            'rating',
            'is_available',
            
        )


class CarModelSerializer(ModelSerializer):

    class Meta:
        model = models.CarModel
        fields = (
            'id',
            'name',
            'manufacturer',
            'production_year',
            'price',
            'is_available',
            
        )


