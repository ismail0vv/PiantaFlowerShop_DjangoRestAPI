from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import User

from .models import *


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = "__all__"

    def validate_title(self, title):
        if title.startswith('#') and len(title) == 7 and title[1:].isalnum():
            return title
        raise ValidationError('Color title have wrong pattern, must be color hex code')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


SIZE_CHOICES = ('SM', 'MD', 'L', 'XL', 'XXL')


class FlowerSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    categories = CategorySerializer(many=True)
    photos = serializers.SerializerMethodField(many=True)
    size = serializers.ChoiceField(choices=SIZE_CHOICES)

    class Meta:
        model = Flower
        fields = ('title', 'price', 'description', 'categories', 'colors', 'sold_quantity', 'size', 'photos')

    def get_photos(self, flower):
        return flower.get_photos_list()


class FlowerValidateSerializer(serializers.Serializer):
    colors = serializers.ListField(required=True)
    categories = serializers.ListField(required=True)
    photos = serializers.ListField(required=True)
    size = serializers.ChoiceField(choices=SIZE_CHOICES)
    description = serializers.CharField(max_length=255)
    sold_quantity = serializers.IntegerField(default=0)

    def validate_colors(self, colors):
        if len(colors) == Color.objects.filter(id__in=colors).count():
            return colors
        raise ValidationError("some of given colors does not exitst")

    def validate_categories(self, categories):
        if len(categories) == Category.objects.filter(id__in=categories).count():
            return categories
        raise ValidationError("some of given categories does not exists")

    def validate_photos(self, photos):
        if len(photos) == Photo.objects.filter(id__in=photos).count():
            return photos
        raise ValidationError("some of given photos does not exists")

    def validate_size(self, size):
        if size in SIZE_CHOICES:
            return size
        raise ValidationError("wrong size given")


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewValidateSerializer(serializers.Serializer):
    author_id = serializers.IntegerField(min_value=1)
    title = serializers.CharField(max_length=50)
    text = serializers.CharField(max_length=255)
    stars = serializers.IntegerField(min_value=0, max_value=10)

    def validate_author_id(self, author_id):
        author_exists = User.objects.filter(id=author_id).exists()
        if author_exists:
            return author_id
        raise ValidationError('Author does not exists')
