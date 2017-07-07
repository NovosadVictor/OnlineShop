from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from cart.models import ProductInCart


class OrderView(APIView):

    def post(self, request):
        user = get_object_or_404(User, id=request.data['user_id'])
        products = user.products_in_cart.all()
        products_text = ' ,'.join(str(item.product.name) for item in products)
        Order.objects.create(customer=user,
                             products=products_text,
                             delivery=bool(request.data['delivery']))
        ProductInCart.objects.filter(owner=user).delete()
        return Response('"Error":""')



# Create your views here.
