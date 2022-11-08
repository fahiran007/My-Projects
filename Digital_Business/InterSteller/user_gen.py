import random
from InterSteller.models import signup
items = ['1234567890']
def user_gen():
    i = 1
    token = ''
    for i in range(7):
        catchNumber = 0
        code = random.choice(items[catchNumber])
        token = token + code
    if signup.objects.filter(refer=token).first():
        user_gen()
    return token