from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CartSerializer
from .models import ProductInCart
from shop.models import Product


class UserCartView(APIView):

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        products = user.products_in_cart.all()
        serializer = CartSerializer(products, many=True)
        return Response(serializer.data)


class AddView(APIView):

    def post(self, request):
        user = get_object_or_404(User, id=request.data['user_id'])
        product = get_object_or_404(Product, id=request.data['product_id'])
        ProductInCart.objects.create(owner=user,
                                     product=product,
                                     quantity=request.data['quantity'])
        product.stock -= request.data['quantity']
        if product.stock <= 0:
            product.available = False
        product.save()
        return Response('"Error":""')


class DeleteView(APIView):

    def post(self, request):
        user = get_object_or_404(User, id=request.data['user_id'])
        product = get_object_or_404(Product, id=request.data['product_id'])
        item = ProductInCart.objects.get(owner=user, product=product)
        product.stock += item.quantity
        product.save()
        item.delete()
        return Response('"Error":""')

class ClearView(APIView):

    def post(self, request):
        user = get_object_or_404(User, id=request.data['user_id'])
        products = ProductInCart.objects.filter(owner=user)
        for item in products:
            if item.product.available is not True:
                item.product.available = True
            item.product.stock += item.quantity
            item.product.save()
        products.delete()
        return Response('"Error":""')



# Create your views here.
