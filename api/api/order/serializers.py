from rest_framework import serializers

from api.order.models import Order
from api.order.validators import validate_only_numbers


class OrderSerializer(serializers.ModelSerializer):
    """

    """
    customer_first_name = serializers.CharField(max_length=30)
    customer_phone = serializers.CharField(validators=[validate_only_numbers, ])

    class Meta:
        model = Order
        fields = (
            "customer_first_name",
            "customer_last_name",
            "customer_phone",
            "customer_email_address",
            "customer_comment",
            "product",
            "comment",
            "status",
            "created_at",
            "updated_at"
        )
