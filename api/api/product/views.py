from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
)

from api.product.models import Category, Product
from api.product.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(RetrieveModelMixin, GenericViewSet, ListModelMixin):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class ProductViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):

    serializer_class = ProductSerializer


    def get_queryset(self):
        return Product.objects.all()
