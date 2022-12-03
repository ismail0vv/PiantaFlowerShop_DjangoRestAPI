from rest_framework import serializers
from .models import *


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class FlowerSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    categories = CategorySerializer(many=True)
    photos = serializers.SerializerMethodField(many=True)

    class Meta:
        model = Flower
        fields = '__all__'

    def get_photos(self, flower):
        return flower.get_photos_list()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
