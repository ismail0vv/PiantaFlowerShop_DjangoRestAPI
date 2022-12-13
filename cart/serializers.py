from rest_framework import serializers
from .models import *
from rest_framework.serializers import ValidationError


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemValidateSerializer(serializers.Serializer):
    flower_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1)

    def validate_flower_id(self, flower_id):
        flower_exists = Flower.objects.filter(id=flower_id).exists()
        if flower_exists:
            return flower_id
        raise ValidationError('Given flower does not exists')


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = 'id user items total_price'.split(' ')

    def get_items(self, cart):
        return cart.cart_items_list()

    def get_total_price(self, cart):
        return cart.total_price()
