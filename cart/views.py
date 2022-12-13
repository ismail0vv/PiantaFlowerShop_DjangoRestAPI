from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Cart, CartItem
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework import status


# Create your views here.
class CartViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (JWTAuthentication,)


class CartAddView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CartItemValidateSerializer

    def post(self, request: Request, *args, **kwargs):
        cart_exists = Cart.objects.filter(user=request.user).exists()
        if not cart_exists:
            Cart.objects.create(user=request.user)
        serializer = CartItemValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        flower_exists = CartItem.objects.filter(flower_id=serializer.validated_data['flower_id']).exists()
        if not flower_exists:
            CartItem.objects.create(cart=Cart.objects.get(user=request.user),
                                    flower_id=serializer.validated_data['flower_id'],
                                    quantity=serializer.validated_data['quantity'])
        else:
            CartItem.objects.get(flower_id=serializer.validated_data['flower_id']).add_quantity(
                serializer.validated_data['quantity'])

        return Response({"message": "added"})


class CartClearView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CartItemSerializer

    def get(self, request: Request, *args, **kwargs):
        return Response({"message": "Are you sure you want to clear cart?"})

    def post(self, request: Request, *args, **kwargs):
        Cart.objects.get(user=request.user).items.all().delete()
        return Response({"message": "successfully cleared"})


class CartOrderView(generics.GenericAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    def post(self, request, *args, **kwargs):
        items = Cart.objects.get(user=request.user).items.all()
        for item in items:
            Flower.objects.get(id=item.flower_id).add_solded(item.quantity)

        Cart.objects.get(user=request.user).items.all().delete()
        return Response({"message": "ordered successfully"})


class CartAPIView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = CartSerializer(Cart.objects.get(user=request.user), many=False)

        return Response(data=serializer.data)


class CartItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer
    authentication_classes = (JWTAuthentication,)
    queryset = CartItem.objects.all()
