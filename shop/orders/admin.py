from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'products', 'created', 'updated', 'delivery',]
    list_editable = ['delivery',]
    list_filter = ['customer', 'created', 'delivery',]
admin.site.register(Order)

# Register your models here.
