from django.urls import path, include
from api.order.views import OrderViewSet

app_name = "orders"

urlpatterns = [
    path(r"order/", OrderViewSet.as_view(), name="create_order")
]
