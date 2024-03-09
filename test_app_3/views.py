from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError as DRFValidationError  # To avoid mixing between core validation error
from test_app_3 import models
from test_app_3 import serializers


class EventScheduleView(ModelViewSet):
    queryset = models.EventSchedule.objects.all()
    serializer_class = serializers.EventScheduleSerializer


class ProductCategoryView(ModelViewSet):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer

    @action(methods=['get', 'post'], detail=True)
    def analyze_product_category(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @action(methods=['get', 'post'], detail=False)
    def list_or_create_analysis_product_category(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

