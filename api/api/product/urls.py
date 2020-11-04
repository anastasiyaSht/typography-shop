from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.product import views

app_name = "product"

router = DefaultRouter()
router.register(r"category", views.CategoryViewSet, basename="category")
router.register(r"product", views.ProductViewSet, basename="product")

urlpatterns = [path("", include(router.urls))]
