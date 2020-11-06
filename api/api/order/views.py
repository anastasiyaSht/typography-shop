from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.order.models import Order
from api.order.serializers import OrderSerializer


class OrderViewSet(GenericAPIView):

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = Order(**serializer.validated_data)
        order.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
