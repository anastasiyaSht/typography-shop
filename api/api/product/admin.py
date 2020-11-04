from django.contrib import admin

from api.product.models import Category, Product


admin.site.register(Category)
admin.site.register(Product)
