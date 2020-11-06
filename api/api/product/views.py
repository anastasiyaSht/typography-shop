from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from api.product.models import Category, Product
from api.product.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(RetrieveModelMixin, GenericViewSet, ListModelMixin):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    @action(detail=True, methods=["get"], name="products")
    def products(self, request, pk, *args, **kwargs):
        category = self.get_object()
        data = ProductSerializer(category.products.all(), many=True).data

        return Response(data, status=status.HTTP_200_OK)


class ProductViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
