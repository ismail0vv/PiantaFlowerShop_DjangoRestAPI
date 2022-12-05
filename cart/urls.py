from django.urls import path, include
from .views import CartItemViewSet, CartViewSet
from rest_framework.routers import SimpleRouter

ROUTER = SimpleRouter()
ROUTER.register(r'carts', CartViewSet)
ROUTER.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path("", include(ROUTER.urls), name="cart_api")
]