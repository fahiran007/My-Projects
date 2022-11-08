# Install Courier SDK: pip install trycourier
from trycourier import Courier

client = Courier(auth_token="pk_prod_WJTXYHHP594DP0GG8B4FSZBCME0E")
from random import randint
def send_mail(recepent):
   code = ""
   for i in range(6):
       code += str(randint(0, 9))
   resp = client.send_message(
     message={
       "to": {
         "email": "fffahiran@gmail.com"
       },
       "content": {
         "title": "Welcome to Courier!",
         "body": "Your verification code is {{code}}"
       },
       "data":{
           'code':code
       }
     }
   )
   return code