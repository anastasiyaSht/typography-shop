from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.product.models import Category, Product
from api.product.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(GenericViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

    @action(detail=False, methods=["get"], name="categories")
    def categories(self, request, *args, **kwargs):
        data = CategorySerializer(self.get_queryset()).data
        return Response(data)

    @action(detail=True, methods=["get"], name="category")
    def category(self, request, pk=None, *args, **kwargs):
        if not pk:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category = self.get_object()
        data = CategorySerializer(category).data
        return Response(data)
