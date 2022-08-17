import http.client

import requests
from extensions.code_generator import otp_generator
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings

# send otp code 
def send_otp(*, user_otp: object, phone: str):
    otp = otp_generator()
    user_otp.otp = otp
    url = f'http://notify.eskiz.uz/api/message/sms/send?mobile_phone={phone}&from=4546&message=sts-hik.uz kirish uchun parol:{otp}'
    http.client.HTTPSConnection("notify.eskiz.uz")
    files = []
    headers = {'Authorization': f'Bearer {settings.SMS_TOKEN}'}


    response = requests.request("POST", url, headers=headers,  files=files)
    user_otp.count+=1
    user_otp.save(update_fields=['otp','count'])

    return Response(
        response.json(),
        status=status.HTTP_200_OK,
    )
