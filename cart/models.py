from django.db import models
from Pianta import settings
from flower.models import Flower


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
