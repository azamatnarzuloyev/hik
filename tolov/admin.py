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
        "order__user__phone",
    ]
    list_filter= [
        'status'
    ]
    empty_value_display = '-empty-'
    date_hierarchy = 'date'
    list_editable = ['status']
    list_per_page = 20
    list_select_related = ['order']
    ordering = ['-date']
    list_display_links = ['order', 'amount']
    radio_fields = {"status":admin.HORIZONTAL}
    
admin.site.register(OrderPayment, OrderPaymentAdmin)
