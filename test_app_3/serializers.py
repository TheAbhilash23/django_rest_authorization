from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_3 import models


class EventScheduleSerializer(ModelSerializer):

    class Meta:
        model = models.EventSchedule
        fields = (
            'id',
            'name',
            'location',
            'start_datetime',
            'end_datetime',
            'is_public',
            
        )


class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model = models.ProductCategory
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock_quantity',
            'is_available',
            
        )


