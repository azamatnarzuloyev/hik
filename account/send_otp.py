import http.client

import requests
from django.core.cache import cache
from extensions.code_generator import otp_generator
from rest_framework import status
from rest_framework.response import Response


# send otp code 
def send_otp(*, user_otp: object, phone: str):
    otp = otp_generator()
    user_otp.otp = otp
    # cache.set(phone, otp, settings.EXPIRY_TIME_OTP)
    # external_api_url = f'https://api.telegram.org/bot5245455385:AAGIxYYiHeul7EqguviPZtprUbzu_Te-Zh4/sendMessage?chat_id=-1001638264258&parse_mode=html&text="{otp}"'
    # res = requests.post(external_api_url)    
    url = f'http://notify.eskiz.uz/api/message/sms/send?mobile_phone={phone}&from=4546&message=sts-hik.uz kirish uchun parol:{otp}' 
    conn = http.client.HTTPSConnection("notify.eskiz.uz")
    files = []
    headers= {'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgyOCwicm9sZSI6InVzZXIiLCJkYXRhIjp7ImlkIjo4MjgsIm5hbWUiOiJPT08gU01BUlQgVEVDSE5PTE9HWSBTWVNURU1TIiwiZW1haWwiOiJhemFtYXRzYWJpbmExNzk2QG1haWwucnUiLCJyb2xlIjoidXNlciIsImFwaV90b2tlbiI6ImV5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUp6ZFdJaU9qZ3lPQ3dpY205c1pTSTZJblZ6WlhJaUxDSmtZWFJoSWpwN0ltbGtJam80TWpnc0ltNWhiV1VpT2lKUFQwOGdVMDFCVWxRZ1ZFVkRTRTVQVEU5SFdTQlRXVk5VUlUxVElpd2laVzFoYVd3aU9pSmhlbUZ0WVhSellXSnBibUV4TnprMlFHMWhhV3d1Y25VaUxDSnliMnhsSWpvaWRYTmxjaUlzSW1Gd2FWOTBiMnRsYmlJNmJuVnNiQ3dpYzNSaGRIVnpJam9pWVdOMGFYWmxJaSIsInN0YXR1cyI6ImFjdGl2ZSIsInNtc19hcGlfbG9naW4iOiJlc2tpejIiLCJzbXNfYXBpX3Bhc3N3b3JkIjoiZSQkayF6IiwidXpfcHJpY2UiOjUwLCJ1Y2VsbF9wcmljZSI6NTAsImJhbGFuY2UiOjI4NDY1MCwiaXNfdmlwIjowLCJob3N0Ijoic2VydmVyMSIsImNyZWF0ZWRfYXQiOiIyMDIyLTA0LTI3VDA1OjI1OjM1LjAwMDAwMFoiLCJ1cGRhdGVkX2F0IjoiMjAyMi0wOC0xMlQwNjozNzo1Mi4wMDAwMDBaIn0sImlhdCI6MTY2MDI4NjQ3OCwiZXhwIjoxNjYyODc4NDc4fQ.dM6yrW5JcT8KbHklPom34zWhxBdTv5Bul9Ni1eNDXLU'}


    response = requests.request("POST", url, headers=headers,  files=files)
    user_otp.count+=1
    user_otp.save(update_fields=['otp','count'])
    print(response.text)
    
    return Response(
 
        response.json(),
        status=status.HTTP_200_OK,
    )
