from rest_framework import serializers
from .models import *


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = 'user items total_price'.split(' ')

    def get_items(self, cart):
        return cart.cart_items_list()

    def get_total_price(self, cart):
        return cart.total_price()
