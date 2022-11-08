import random
items = ['ABCDEFGHIJKLMNOPQrSTUVWXY','abcdefghijklmnopqrstuvwxyz','1234567890']
def token_gen():
    i = 1
    token = ''
    for i in range(30):
        catchNumber = random.randint(0, 2)
        code = random.choice(items[catchNumber])
        token = token + code
    return token