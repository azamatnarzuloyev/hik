from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress
# Register your models here.
# admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
@admin.register(Order)
class OrdersModelAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "taxPrice",
        'shippingPrice',
        'isPaid',
        'paidAt',
        'isDelivered',
      
    ]
    search_fields = [
        "user",
      ]


@admin.register(OrderItem)
class OrderItemsModelAdmin(admin.ModelAdmin):
    list_display = [
   
        "order",
        'name',
        'qty',
        'price',  
    ]
    search_fields = [
        "name",
      ]
     