from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_1 import models
from test_app_1 import serializers


class BookCategoryView(ModelSerializer):
    queryset = models.BookCategory.objects.all()
    serializer_class = serializers.BookCategorySerializer


class CarModelView(ModelSerializer):
    queryset = models.CarModel.objects.all()
    serializer_class = serializers.CarModelSerializer


