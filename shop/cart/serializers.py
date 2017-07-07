from rest_framework import serializers
from .models import ProductInCart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        exclude = ['owner',]