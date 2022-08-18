from asyncio.log import logger
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz
from .models import OrderPayment


class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        """
        Check paid order: if click payment is valid
        :param order_id: order id
        :param amount: amount
        :return: if order found and amount is valid return ORDER_FOUND, else return ORDER_NOT_FOUND
        :rtype: if order found but amount is not valid return INVALID_AMOUNT
        """
        try:
            print(f'check_order: {order_id}  {amount}')
            order = OrderPayment.objects.get(id=int(order_id))
            if float(order.amount) == float(amount):
                order.status = 1
                return self.ORDER_FOUND
            else:
                order.status = 3
                return self.INVALID_AMOUNT
        except Exception as e:
            logger.error(e)
            return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        """
        Successfully payment: if clint paid order successfully: 
        We can change order status to paid True in this method
        :param order_id: order id
        :param transaction: transaction object
        :return: None
        """
        try:
            print(f'successfully_payment: {order_id}  {str(transaction)}')
            order = OrderPayment.objects.get(id=int(order_id))
            user = order.user
            user.cash += order.amount
            user.save()
            order.status = 2
            order.save()
        except Exception as e:
            logger.error(e)
    
    def cancel_payment(self, order_id: str, transaction: object):
        """
        Cancel payment: if clint cancel payment
        :param order_id: order id
        :param transaction: transaction object
        """
        try:
            print(f'cancel_payment: {order_id}  {str(transaction)}')
            order = OrderPayment.objects.get(id=int(order_id))
            order.status = 3
            order.save()
        except Exception as e:
            logger.error(e)

class TestView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment
