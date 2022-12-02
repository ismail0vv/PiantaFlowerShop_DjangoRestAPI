from django.db import models
from Pianta import settings


# Create your models here.
# Моделька Цветов (flower)
# title
# price
# description
# categories ManyToMany
# colors ManyToMany
# sold_quantity


class Category(models.Model):
    title = models.CharField(max_length=30)


class Color(models.Model):
    title = models.CharField(max_length=30)

# Моделька Фото
# flower Foreign Key related_name
# image = ImageField


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    stars = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
