from django.db import models


ORDER_STATUS_CHOICES = (
    (0, "New"),
    (1, "In progress"),
    (2, "Done"),
)


class OrderModel(models.Model):
    """

    """
    customer_first_name = models.CharField(max_length=30)
    customer_last_name = models.CharField(max_length=50, blank=True, null=True)

    customer_phone = models.CharField(max_length=20)
    customer_email_address = models.EmailField(max_length=100, blank=True, null=True)

    comment = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=0)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order №{self.id}"

    class Meta:
        verbose_name = "Order"
