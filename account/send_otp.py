from telnetlib import SEND_URL
from django.core.cache import cache
from django.conf import settings

from rest_framework.response import Response
from rest_framework import status
import requests
from extensions.code_generator import otp_generator


# send otp code 

def send_otp(*, user_otp: object, phone: str):
    otp = otp_generator()
    user_otp.otp = otp
    cache.set(phone, otp, settings.EXPIRY_TIME_OTP)
    external_api_url = f'https://api.telegram.org/bot5245455385:AAGIxYYiHeul7EqguviPZtprUbzu_Te-Zh4/sendMessage?chat_id=-1001638264258&parse_mode=html&text="{otp}"'
    res = requests.post(external_api_url)
   
    # link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=fc9e5177-b3e7-11e8-a895-0200cd936042&to={phone}&from=wisfrg&templatename=wisfrags&var1={otp_key}'
   
    # result = requests.get(link, verify=False)

    # return otp
    # Here the otp code must later be sent to the user's phone number by SMS system.
    print(f"your phone: {phone}")
    print(f"your otp code :: {otp} ")
    # But in debug mode we print the otp code.
    
    user_otp.count += 1
    user_otp.save(update_fields=["otp", "count"])
    context = {
        "code sent.": "The code has been sent to the desired phone number.",
    }
    return Response(
 
        res.json(),
        status=status.HTTP_200_OK,
    )
    # return Response(context,res.json())
