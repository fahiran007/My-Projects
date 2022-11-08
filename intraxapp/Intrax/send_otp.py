from random import randint
def Send_email_and_phone_otp(email,phone):
    email_otp = ""
    phone_otp = ""
    for i in range(6):
        email_otp += str(randint(0, 9))
        phone_otp += str(randint(0, 9))
    return email_otp,phone_otp
    
