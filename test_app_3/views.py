from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_3 import models
from test_app_3 import serializers


class EventScheduleView(ModelSerializer):
    queryset = models.EventSchedule.objects.all()
    serializer_class = serializers.EventScheduleSerializer


class ProductCategoryView(ModelSerializer):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer


