from rest_framework.response import Response
from .serializers import CartItemSerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Cart, CartItem
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class CartViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (JWTAuthentication,)


class CartAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CartSerializer(data=Cart.objects.get(user=request.user))
        serializer.is_valid(raise_exception=True)

        return Response(data=serializer.data)


class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    authentication_classes = (JWTAuthentication,)
    queryset = CartItem.objects.all()
