from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress, OrderPayment
# Register your models here.

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

class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "amount",
        "status",
        "date",
    ]
    search_fields = [
        "order",
    ]
    list_filter= [
        'status'
    ]
    date_hierarchy = 'date'

admin.site.register(OrderPayment, OrderPaymentAdmin)