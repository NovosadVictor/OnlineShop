from django.contrib import admin
from .models import ProductInCart


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ['owner', 'product', 'quantity',]
    list_editable = ['quantity',]
admin.site.register(ProductInCart, ProductInCartAdmin)
