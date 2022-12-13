from django.urls import path, include
from cart import views
from rest_framework.routers import SimpleRouter

ROUTER1 = SimpleRouter()
ROUTER2 = SimpleRouter()
ROUTER1.register(r'carts-crud', views.CartViewSet)
ROUTER2.register(r'cart-item', views.CartItemViewSet)

urlpatterns = [
    path("", include(ROUTER1.urls), name="cart-api"),
    path('', include(ROUTER2.urls), name="cart-item-api"),
    path('cart/', views.CartAPIView.as_view(), name="get-user-cart"),
    path('cart/add/', views.CartAddView.as_view(), name="add-to-cart"),
    path('cart/clear/', views.CartClearView.as_view(), name="claer-user-cart"),
    path('cart/order/', views.CartOrderView.as_view(), name='order-user-cart')
]