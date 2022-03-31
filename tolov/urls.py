from django.urls import path
import tolov.views as views
app_name = "tolov"
urlpatterns = [
    path('', views.getOrders, name='orders'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('add/', views.addOrderItems, name='order-add'),
    path('<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]