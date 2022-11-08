from django.db import models

# Create your models here.
class Application_Form(models.Model):
    app_title = models.CharField(max_length=1000)
    app_subtitle = models.CharField(max_length=1000)
    app_link = models.CharField(max_length=1000)
    def __str__(self):
        return self.app_title
class CreateForm(models.Model):
    Name = models.CharField(default=None,max_length=300)
    Email = models.CharField(default=None,max_length=300)
    Phone = models.CharField(default=None,max_length=300)
    Password = models.CharField(default=None,max_length=300)
    Re_pass = models.CharField(default=None,max_length=300)
    idx = models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.Name
class FormValidation(models.Model):
    Name = models.CharField(default=None,max_length=300)
    Email = models.CharField(default=None,max_length=300)
    Phone = models.CharField(default=None,max_length=300)
    Password = models.CharField(default=None,max_length=300)
    Re_pass = models.CharField(default=None,max_length=300)
    idx = models.CharField(max_length=50,default=None)
    email_otp = models.CharField(max_length=50,default=0)
    phone_otp = models.CharField(max_length=50,default=0)
    def __str__(self):
        return self.Name