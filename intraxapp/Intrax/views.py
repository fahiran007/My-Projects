from django.shortcuts import render
from .models import Application_Form,CreateForm,FormValidation
from django.contrib.auth import login,authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from . import idx_gen
from django.http import HttpResponse
from .send_otp import Send_email_and_phone_otp
# Create your views here.
def home(request):
    if request.user.is_anonymous:
        return redirect('/Intrax/Login')
    else:
        data = Application_Form.objects.all()
    return render(request, 'index.html',{'data':data})
def Login(request):
    try:
        Phone = request.GET.get('Phone')
        Password = request.GET.get('Password')
        if Phone!=None and Password!=None:
            data = {
                'phone':Phone,
                'pass':Password
            }
            user = authenticate(username=Phone,password=Password)
            if user is not None:
                error = "Your Account Was Created successfully"
            elif user is None :
                error = "Phone/Password Phone or Password is incorrect"
            return render(request, 'Intrax/login.html',{'error':error,'data1':data})
    except Exception as f:
        pass
    return render(request, 'Intrax/login.html')
def Create_Account(request):
    if request.method == "POST":
        Name = request.POST.get('Name')
        Phone = request.POST.get('Phone')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Re_pass = request.POST.get('Re_pass')
        idx = idx_gen.token_gen()
        data = {
            'phone':Phone,
            'email':Email,
            'pass':Password,
            're_pass':Re_pass,
            'name':Name
        }
        if str(Email).find('@gmail.com') != -1:
            pass
        else:
            return render(request, 'login.html',{'error':"Your entered email address is invalid Please enter a valid Email Address",'data':data})
        if Password == Re_pass:
            pass
        else:
            return render(request, 'login.html',{'error':"Your entered passwords was does not Match",'data':data})
        if str(Password).__len__() <8:
            return render(request, 'login.html',{'error':'Your entered password was too short Please enter a long password ','data':data})
        if FormValidation.objects.filter(Email=Email).first():
            return render(request, 'login.html',{'error':"Your entered email address is already exists Please enter a new email address",'data':data})
        if FormValidation.objects.filter(Phone=Phone).first():
            return render(request, 'login.html',{'error':"Your entered Phone number is already exists Please enter a new Phone number address",'data':data})
        email_otp,phone_otp = Send_email_and_phone_otp('email', 'phone')
        userInfo = FormValidation(Name=Name,Email=Email,Password=Password,Re_pass=Re_pass,Phone=Phone,idx=idx,phone_otp=phone_otp,email_otp=email_otp)
        userInfo.save()
        return redirect(f'/OTP-Verification')
    return render(request, 'Intrax/login.html')
def Verification(request):
    Phone_number = request.GET.get('phone')
    try :
        Email_OTP = request.GET.get('em-otp')
        Phone_OTP = request.GET.get('ph-otp')
        if Phone_OTP!=None and Email_OTP!=None:
            if FormValidation.objects.filter(phone_otp=Phone_OTP,email_otp=Email_OTP).first():
                pass
            else:
                print('OTP not matched')
                return render(request, 'login.html',{'error':'Your entered Email OTP invalid, Please enter a valid OTP','em_otp':Email_OTP,'ph_otp':Phone_OTP})
            if datas.phone_otp == Phone_OTP:
                return render(request, 'login.html',{'error':'C'})
            else:
                return render(request, 'login.html',{'error':'Your entered Phone OTP invalid, Please enter a valid OTP','em_otp':Email_OTP,'ph_otp':Phone_OTP})
    except:
        pass
    return render(request, 'login.html')