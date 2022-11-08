import random
from InterSteller.models import signup
items = ['ABCDEFGHIJKLMNOPQRSTUVWXY','1234567890']
def refer_gen():
    i = 1
    token = ''
    for i in range(7):
        catchNumber = random.randint(0, 1)
        code = random.choice(items[catchNumber])
        token = token + code
    if signup.objects.filter(refer=token).first():
        refer_gen()
    return token