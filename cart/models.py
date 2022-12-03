from django.db import models

# Create your models here.
# Корзина Cart
# user пользователь
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Моделька CartItem
# cart foreignKey корзина
# flower цветы берешь модельку ForeignKey
# quantity количество
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
