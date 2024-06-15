from django.urls import path, include
from rest_framework import routers
from .views import (
    ProductViewSet, OptionListViewSet, OptionViewSet, CartViewSet, CartItemViewSet, OrderViewSet
)

router = routers.DefaultRouter()

router.register(r'products', ProductViewSet)
router.register(r'option-lists', OptionListViewSet)
router.register(r'options', OptionViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
