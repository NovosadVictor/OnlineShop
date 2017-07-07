# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer


class CategoriesView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductsView(APIView):

    def get(self, request, category=0):
        if category == 0:
            products = Product.objects.filter(available=True)
        else:
            products = Product.objects.filter(available=True, category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):

    def get(self, request, category, slug):
            product = get_object_or_404(Product, category=category, slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

