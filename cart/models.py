from django.db import models
from Pianta import settings
from flower.models import Flower


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def cart_items_list(self):
        return [{ "id": item.id, "cart_id": item.cart_id, "flower_id": item.flower_id, "quantity": item.quantity } for
                item in self.items.all()]

    def total_price(self):
        return sum([item.price() for item in self.items.all()])

    def __str__(self):
        return self.user.email + ' cart'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def price(self):
        return self.flower.price * self.quantity

    def __str__(self):
        return str(self.cart) + 'cart item'

    def add_quantity(self, amount):
        self.quantity += amount
        self.save()
