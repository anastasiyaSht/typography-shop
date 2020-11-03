from django.contrib import admin

from api.order.models import OrderModel


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_first_name", "customer_phone", "status", "created_at", "updated_at")

    search_fields = ("id", "customer_first_name", "customer_last_name",  "customer_phone", "customer_email_address")
    list_filter = ("status", )


admin.site.register(OrderModel, OrderAdmin)
