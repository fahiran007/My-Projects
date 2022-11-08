from django.shortcuts import render,redirect
from InterSteller.models import signup,products,Transactions,Helps,SignupChecking
from InterSteller.send_otp import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from InterSteller.user_auth import authonticate
from . import idx_gen,refer_gen,user_gen
import datetime
from random import randint
# Create your views here.
Email = None
Password = None

def index(request):
    if request.user.is_anonymous:
        return redirect("/userlogin")
    else:
        return redirect('/userlogin')
    return render(request, 'index.html',{"data":items})
def index2(request,idx):
    userdata = signup.objects.get(idx=idx)
    items = products.objects.all()
    return render(request, 'index.html',{"data":items,'idx':idx})
def usercreate(request,refer_code):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        Re_pass = request.POST.get('repass')
        referfrom = request.POST.get('referBy')
        Money = 0
        idx = idx_gen.token_gen()
        refer = refer_gen.refer_gen()
        UserId = user_gen.user_gen()
        if signup.objects.filter(refer_by=referfrom).first():
            pass
        else:
            return render(request, 'signup.html',{'idx':idx,'refer':'invalid','refer_code':refer_code})
        if User.objects.filter(username = Email).first():
            if Password != Re_pass:
                return render(request, 'signup.html',{'pass_status':'notmatch','status':'invalid','refer_code':refer_code})
            else:
                return render(request, 'signup.html',{'status':'invalid','refer_code':refer_code})
        if str(Password).__len__() < 8:
            return render(request, 'signup.html',{'short':'too','refer':refer_code})
        elif Password!=Re_pass:
            return render(request, 'signup.html',{'pass_status':'notmatch','refer_code':refer_code})
        # verify = send_mail(Email)
        # verify = send_mail(Email)
        verify = 123
        userdetails = SignupChecking(verification=verify,Names=Name,UserId=UserId,Passwords=Password,Emails=Email,Moneys=Money,idx=idx,refer_by=referfrom,refer=refer)
        userdetails.save()
        return redirect(f'/otp_verify/{UserId}')
    return render(request, 'signup.html',{'refer_code':refer_code})
def user_login(request):
    if request.method == 'POST':
        global email,password
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email,password=password)
        if user is not None:
            user_data = signup.objects.filter(Emails=email,Passwords=password).values()
            print(user_data)
            for item in user_data:
                idx = item['idx']
                login(request, user)
                return redirect(f'/index/{idx}')
        else:
            return render(request, 'login.html',{'login':'not'})
        
    return render(request, 'login.html')
def otp_verificattion(request,UserID):
    usercheking = SignupChecking.objects.get(UserId=UserID)
    infos = {
        'data':usercheking.Emails,
        'UserId':idx,
        'otp':'valid',
        'link':'/otp_verify',
        'idx':'SignUP',
        'refer':'valid'
             }
    for i in range(8):
            trans_id = randint(1, 9)
            ids =ids+ str(trans_id)
    transact = Transactions(idx=idx2,amount=30,types='r',status='s',transID=ids,date=datetime.date.today())
    transact.save()
    if request.method == 'POST':
        otp = request.POST.get('otp')
        # try:
        if usercheking.verification == str(otp):
            Name   = usercheking.Names
            Email = usercheking.Emails
            Password = usercheking.Passwords
            Money = usercheking.Moneys
            verify = usercheking.verification
            idx = usercheking.idx
            refer = usercheking.refer
            referfrom = usercheking.refer_by
            UserId = usercheking.UserId
            user_details = signup(Names=Name,UserId=UserId,Passwords=Password,Emails=Email,Moneys=Money,idx=idx,refer_by=referfrom,refer=refer)
            user_id,created = User.objects.get_or_create(username=Email)
            user_id.set_password(Password)
            user_id.save()
            user_details.save()
            return redirect('/userlogin')
        else:
             infos['otp'] = 'Invalid'
             return render(request, 'otp_verify.html',infos)
        # except:
        #     return redirect('/Intersteller/None')
    return render(request, 'otp_verify.html',infos)
def products_info(request,idx1,idx):
    main_pro = products.objects.filter(idx=idx1).values()
    return render(request, 'product_info.html',{'idx':idx,'idx1':idx1,'datas':main_pro})
def Account(request,idx):
    userdata = signup.objects.get(idx=idx)
    profile_pic = userdata.profile
    Account_info = signup.objects.filter(idx=idx)
    return render(request, 'Account.html',{'data':Account_info,'idx':idx})
def Account2(request,idx,mode):
    if mode == 'w':
        data = signup.objects.get(idx=idx)
        final_money = data.Moneys
        data2 = Transactions.objects.filter(types='w',idx=idx).values()
        return render(request, 'withdrawal.html',{'money':final_money,'idx':idx,'status':'success','datas2':data2})
    elif mode == 'f':
            return render(request, 'forgot_pass.html',{'idx':idx,'changed':'changed'})
    userdata = signup.objects.get(idx=idx)
    profile_pic = userdata.profile
    Account_info = signup.objects.filter(idx=idx)
    return render(request, 'Account.html',{'data':Account_info,'idx':idx})
def Update_info(request,idx):
    if request.method == "POST":
        global new_email,new_name
        new_email = request.POST.get('email')
        new_name = request.POST.get('name')
        if User.objects.filter(username = new_email).first():
            return render(request, 'Update_info.html',{'idx':idx,'status':'invalid'})
        global Update_verify
        Update_verify = 000
        return redirect(f'/Update_otp/{idx}')
    return render(request, 'Update_info.html',{'idx':idx})
def update_otp(request,idx):
    if request.method == "POST":
        otp = request.POST.get('otp')
        print(otp)
        print(Update_verify)
        if Update_verify == int(otp):
            update = signup.objects.get(idx=idx)
            update.Emails = new_email
            update.Names = new_name
            user_updates,create= User.objects.get_or_create(username=new_email)
            user_updates.username = new_email
            user_updates.save()
            update.save()
            return redirect(f'/Account/{idx}')
        else:
            print('OTP NOT MATCH')
            return render(request, 'otp_verify.html',{'idx':idx,'otp':'invalid','link':'/Update_otp'})
    return render(request, 'otp_verify.html',{'link':'/Update_otp','idx':idx})
def withdrawal(request,idx):
    check_amount = 'true'
    data = signup.objects.get(idx=idx)
    data2 = Transactions.objects.filter(types='w',idx=idx).values()
    money = data.Moneys
    ids = ""
    if request.method == 'POST':
        amount = request.POST.get('amount')
        upi_id = request.POST.get('upi_id')
        try:
            amnt = int(amount)
        except:
            return render(request, 'withdrawal.html',{'idx':idx,'amountvalid':'invalid'})
        if int(amount) < 300:
            return render(request, 'withdrawal.html',{'idx':idx,'am':'invalid','datas2':data2})
        if amnt>money:
            return render(request, 'withdrawal.html',{'idx':idx,'nomoney':'nomoney','money':money,'datas2':data2})
        upi_id = request.POST.get('upi_id')
        for i in range(8):
            trans_id = randint(1, 9)
            ids =ids+ str(trans_id)
        user_trans = Transactions(idx=idx,amount=amount,status='p',date=datetime.date.today(),types='w',transID=ids,upi_id=upi_id)
        user_trans.save()
        money = money-amnt
        data.Moneys = money
        data.save()
        data = signup.objects.get(idx=idx)
        final_money = data.Moneys
        # return render(request, 'withdrawal.html',{'money':final_money,'idx':idx,'status':'success','datas2':data2})
        return redirect('/Account/'+idx+"/w")
    return render(request, 'withdrawal.html',{'money':money,'idx':idx,'datas2':data2})
def forgot_pass(request,idx):
    if request.method == "POST":
        old_pass = request.POST.get('password')
        new_pass = request.POST.get('newpassword')
        ReNew_pass = request.POST.get('renewpassword')
        if new_pass != ReNew_pass:
            return render(request, 'forgot_pass.html',{'idx':idx,'status':'notmatch'})
        if str(new_pass).__len__() <8:
                return render(request, 'forgot_pass.html',{'idx':idx,'status':'short'})
        user_pass = signup.objects.filter(idx=idx).values()
        for item in user_pass:
            pas = item['Passwords']
            user_em = item['Emails']
            if pas == old_pass:
                NewUser,created = User.objects.get_or_create(username=user_em)
                NewUser.set_password(new_pass)
                NewUser.save()
                new_update = signup.objects.get(idx=idx)
                new_update.Passwords = new_pass
                new_update.save()
                return redirect('/Account/'+idx+"/f")
            else:
                return render(request, 'forgot_pass.html',{'idx':idx,'pas_stat':'wrong'})
    return render(request, 'forgot_pass.html',{'idx':idx})
def helps(request,idx):
    massage_data = Helps.objects.filter(idx=idx).values()
    if request.method == 'POST':
        message = request.POST.get('massage')
        if str(message).__len__()<=20:
            return render(request, 'helps.html',{'idx':idx,'inv':'invalid','massage_data':massage_data})
        l = Helps(massage=message,idx=idx)
        l.save()
        return redirect(f'/help/{idx}')
    return render(request, 'helps.html',{'idx':idx,'massage_data':massage_data})
def share(request,idx):
    UserData = signup.objects.get(idx=idx)
    referId = UserData.refer
    return render(request, 'share.html',{'idx':idx,'refer':referId})
def about(request,idx):
    return render(request, 'about.html',{'idx':idx})
def LogoutUser(request):
    logout(request)
    return redirect('/')
def transactions(request,idx):
    data = Transactions.objects.filter(idx=idx).values()
    return render(request, 'transaction.html',{'datas':data,"idx":idx})
def ControlPanel(request,password,username):
    user = authenticate(username=username,password=password)
    if user is not None :
        pass
    else:
        return HttpResponse("Your not Not AdminPanel Officer")
    if request.method == 'POST':
        Title = request.POST.get("Title")
        Subtitle = request.POST.get("Subtitle")
        Link = request.POST.get("Link")
        amount = request.POST.get("amount")
        desc = request.POST.get("desc")
        When = request.POST.get("When")
        speci1 = request.POST.get("speci1")
        speci2 = request.POST.get("speci2")
        speci3 = request.POST.get("speci3")
        speci4 = request.POST.get("speci4")
        speci5 = request.POST.get("speci5")
        speci6 = request.POST.get("speci6")
        speci7 = request.POST.get("speci7")
        speci8 = request.POST.get("speci8")
        speci9 = request.POST.get("speci9")
        speci10 = request.POST.get("speci10")
        userdata = products(title=Title,subtitle=Subtitle,link=Link,earn_money=amount,when_get_money=When,descriptions=desc,speci10=speci10,speci8=speci8,speci7=speci7,speci9=speci9,speci4=speci4,speci5=speci5,speci1=speci1,speci2=speci2,speci3=speci3,speci6=speci6,)
    return render(request, 'Home.html')