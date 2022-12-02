from django.db import models
from Pianta import settings


class Flower(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    categories = models.ManyToManyField('Category')
    colors = models.ManyToManyField('Color')
    sold_quantity = models.IntegerField(default=0)


class Category(models.Model):
    title = models.CharField(max_length=30)


class Color(models.Model):
    title = models.CharField(max_length=30)


# Моделька Фото
# flower Foreign Key related_name
# image = ImageField
class Photo(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='photos')

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    stars = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
