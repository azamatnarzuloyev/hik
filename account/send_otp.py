import requests
from django.core.cache import cache
from extensions.code_generator import otp_generator, get_client_ip
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

# send otp code 
def send_otp(request, phone):
    otp = otp_generator()
    ip = get_client_ip(request)
    # user_otp.otp = otp
    cache.set(f"{ip}-for-authentication", phone, settings.EXPIRY_TIME_OTP)
    cache.set(phone, otp, settings.EXPIRY_TIME_OTP)
    # user_otp.otp = otp

    url = f'http://notify.eskiz.uz/api/message/sms/send?mobile_phone={phone}&from=4546&message=sts-hik.uz:kirish uchun parol {otp}'
    headers = {'Authorization': f'Bearer {settings.SMS_TOKEN}'}


    response = requests.post(url, headers=headers)
    return Response(
        response.json(),
        status=status.HTTP_200_OK,
    )
