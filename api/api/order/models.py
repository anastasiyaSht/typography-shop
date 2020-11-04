from django.db import models
from django.utils.translation import gettext_lazy as _

from api.product.models import Product


ORDER_STATUS_CHOICES = (
    (0, _("New")),
    (1, _("In progress")),
    (2, _("Done")),
)


class Order(models.Model):
    """

    """
    customer_first_name = models.CharField(max_length=30, verbose_name=_("Customer's first name"))
    customer_last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Customer's last name"))

    customer_phone = models.CharField(max_length=20, verbose_name=_("Phone number"))
    customer_email_address = models.EmailField(max_length=100, blank=True, null=True, verbose_name=_("Email address"))
    customer_comment = models.TextField(blank=True, null=True, verbose_name=_("Customer's comment to the order"))

    comment = models.TextField(blank=True, null=True, verbose_name=_("Admin's comment"))
    status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=0, verbose_name=_("Status"))

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{_('Order')} №{self.id}"

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
