from django.urls import path

from .click import TestView
from .views import *

app_name = "tolov"

urlpatterns = [
    path('', getOrders, name='orders'),
    path('myorders/', getMyOrders, name='myorders'),
    path('add/', addOrderItems, name='order-add'),
    # path('<str:pk>/deliver/', updateOrderToDelivered, name='order-delivered'),
    # path('<str:pk>/', getOrderById, name='user-order'),
    # path('<str:pk>/pay/', updateOrderToPaid, name='pay'),
    #click payment url
    path('click/transaction/', TestView.as_view()),
    path('create-invoise-click/', create_invoise),

]
