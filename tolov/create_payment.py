from asyncio.log import logger

from clickuz import ClickUz
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import OrderPayment


class ClickTransactionPayment(APIView):
    """
    Create click payment POST
    args: amount, order
    return: url for click `payment
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            order, _ = OrderPayment.objects.get_or_create(
                amount=request.data.get('amount'),
                order_id=request.data.get('order_id')
            )
            url = ClickUz.generate_url(order_id=str(order.id), 
            amount=str(order.amount))
            data = {"success": True,'url': url}
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(e)
            return Response({"success": False,'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

create_click_payment = ClickTransactionPayment.as_view()
