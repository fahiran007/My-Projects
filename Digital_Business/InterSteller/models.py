from django.db import models

# Create your models here.
class SignupChecking(models.Model):
    Names = models.CharField(max_length=50)
    Emails = models.CharField(max_length=50)
    Passwords = models.CharField(max_length=50)
    Moneys = models.IntegerField()
    verification = models.CharField(max_length=50,)
    idx = models.CharField(max_length=500)
    refer = models.CharField(max_length=50)
    refer_by = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50)
    def __str__(self):
        return self.Names
class signup(models.Model):
    Names = models.CharField(max_length=50)
    Emails = models.CharField(max_length=50)
    Passwords = models.CharField(max_length=50)
    Moneys = models.IntegerField()
    verification = models.CharField(max_length=50,)
    idx = models.CharField(max_length=500)
    refer = models.CharField(max_length=50)
    refer_by = models.CharField(max_length=50)
    UserId = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='static', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.Names
class products(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    product_img = models.ImageField(upload_to='static',height_field=None, width_field=None, max_length=None)
    earn_money = models.CharField(max_length=50)
    when_get_money = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=3000)
    link = models.CharField(max_length=50)
    speci1 = models.CharField(max_length=500)
    speci2 = models.CharField(max_length=500)
    speci3 = models.CharField(max_length=500)
    speci4 = models.CharField(max_length=500)
    speci5 = models.CharField(max_length=500)
    speci6 = models.CharField(max_length=500)
    speci7 = models.CharField(max_length=500)
    speci8 = models.CharField(max_length=500)
    speci9 = models.CharField(max_length=500)
    speci10 = models.CharField(max_length=500)
    idx = models.CharField( max_length=500)
    
class Helps(models.Model):
    massage = models.CharField(max_length=50)
    reply = models.CharField(max_length=50)
    idx = models.CharField(max_length=50)
class Transactions(models.Model):
    types = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    amount = models.IntegerField()
    date = models.CharField(max_length=50)
    transID = models.CharField(max_length=50)
    idx = models.CharField(max_length=50)
    upi_id = models.CharField(max_length=50)

