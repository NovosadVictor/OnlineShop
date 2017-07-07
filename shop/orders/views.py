from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from cart.models import ProductInCart


class OrderView(APIView):

    def post(self, request):
        products = request.user.products_in_cart.all()
        products_text = ' ,'.join(str(item.product.name) for item in products)
        Order.objects.create(customer=request.user,
                             products=products_text,
                             delivery=bool(request.data['delivery']))
        ProductInCart.objects.filter(owner=request.user).delete()
        return Response('"Error":""')



# Create your views here.
