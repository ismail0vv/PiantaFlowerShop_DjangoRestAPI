from django.db import models
from Pianta import settings
from flower.models import Flower


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def cart_items_list(self):
        return [item for item in self.items.all()]

    def total_price(self):
        return sum([item.price for item in self.items.all()])


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = flower.price * quantity
