from .serializers import CartItemSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Cart, CartItem
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class CartViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (JWTAuthentication, )


class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    authentication_classes = (JWTAuthentication, )
    queryset = CartItem.objects.all()
