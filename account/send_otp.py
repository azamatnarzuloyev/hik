from django.core.cache import cache
from django.conf import settings
import http.client
import mimetypes
from rest_framework.response import Response
from rest_framework import status
from extensions.code_generator import otp_generator
import requests


# send otp code 

def send_otp(*, user_otp: object, phone: str):
    otp = otp_generator()
    user_otp.otp = otp
    cache.set(phone, otp, settings.EXPIRY_TIME_OTP)
    # external_api_url = f'https://api.telegram.org/bot5245455385:AAGIxYYiHeul7EqguviPZtprUbzu_Te-Zh4/sendMessage?chat_id=-1001638264258&parse_mode=html&text="{otp}"'
    # res = requests.post(external_api_url)    
    url = f'http://notify.eskiz.uz/api/message/sms/send?mobile_phone={phone}&from=4546&message=sts-hik.uz kirish uchun parol:{otp}' 
    conn = http.client.HTTPSConnection("notify.eskiz.uz")
    files = []
    headers= {'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjgyOCwicm9sZSI6InVzZXIiLCJkYXRhIjp7ImlkIjo4MjgsIm5hbWUiOiJPT08gU01BUlQgVEVDSE5PTE9HWSBTWVNURU1TIiwiZW1haWwiOiJhemFtYXRzYWJpbmExNzk2QG1haWwucnUiLCJyb2xlIjoidXNlciIsImFwaV90b2tlbiI6bnVsbCwic3RhdHVzIjoiYWN0aXZlIiwic21zX2FwaV9sb2dpbiI6ImVza2l6MiIsInNtc19hcGlfcGFzc3dvcmQiOiJlJCRrIXoiLCJ1el9wcmljZSI6NTAsImJhbGFuY2UiOjI4NDk1MCwiaXNfdmlwIjowLCJob3N0Ijoic2VydmVyMSIsImNyZWF0ZWRfYXQiOiIyMDIyLTA0LTI3VDA1OjI1OjM1LjAwMDAwMFoiLCJ1cGRhdGVkX2F0IjoiMjAyMi0wNy0wMlQxOToyNToxOC4wMDAwMDBaIn0sImlhdCI6MTY1NzA4MjA0NywiZXhwIjoxNjU5Njc0MDQ3fQ.dc92GrlEShW4P3Uu7jZfiNr0ttGjzC3mLsSQI2mwado'}


    response = requests.request("POST", url, headers=headers,  files=files)
    user_otp.count+=1
    user_otp.save(update_fields=['otp','count'])
    print(response.text)
    
    return Response(
 
        response.json(),
        status=status.HTTP_200_OK,
    )
