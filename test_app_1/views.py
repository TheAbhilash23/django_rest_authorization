from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_1 import models
from test_app_1 import serializers


class BookCategoryView(ModelViewSet):
    queryset = models.BookCategory.objects.all()
    serializer_class = serializers.BookCategorySerializer


class CarModelView(ModelViewSet):
    queryset = models.CarModel.objects.all()
    serializer_class = serializers.CarModelSerializer

    def list(self, request, *args, **kwargs):
        print("THIS IS VIEW")
        return super().list(request, *args, **kwargs)


