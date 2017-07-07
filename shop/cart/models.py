from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class ProductInCart(models.Model):
    owner = models.ForeignKey(User, related_name='products_in_cart')
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ('owner',)
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

    def __str__(self):
        return self.product.name
