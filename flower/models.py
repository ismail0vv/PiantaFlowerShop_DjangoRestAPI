from django.db import models
from Pianta import settings


class Flower(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    categories = models.ManyToManyField('Category')
    colors = models.ManyToManyField('Color')
    sold_quantity = models.IntegerField(default=0)

    def get_photos_list(self):
        return [photo.image for photo in self.photos.all()]


class Category(models.Model):
    title = models.CharField(max_length=30)


class Color(models.Model):
    title = models.CharField(max_length=30)


class Photo(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField()


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    stars = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
