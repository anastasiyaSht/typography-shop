from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """

    """
    title = models.CharField(max_length=30, verbose_name=_("Subcategory title"))
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name=_("Description"))
    image = models.ImageField(upload_to="media/category", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(models.Model):
    """

    """
    title = models.CharField(max_length=30, verbose_name=_("Title"))
    description = models.TextField(max_length=2000, verbose_name=_("Description"))
    image = models.ImageField(upload_to="media/product", blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
