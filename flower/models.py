from django.db import models
from Pianta import settings
from django.contrib.sites.shortcuts import get_current_site

class Flower(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    categories = models.ManyToManyField('Category')
    colors = models.ManyToManyField('Color')
    sold_quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=5)

    def get_photos_list(self):
        return [photo.image.url for photo in self.photos.all()]

    def __str__(self):
        return self.title

    def add_solded(self, amount):
        self.sold_quantity += amount
        self.save()



class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Photo(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField()

    def __str__(self):
        return self.flower.title + ' photo'


class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=255)
    stars = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author.__str__() + ' ' + self.title
