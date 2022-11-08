"""Digital_Business URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from InterSteller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('otp_verify/<str:UserID>',views.otp_verificattion,name="otp_verify"),
    path('userlogin',views.user_login,name="userlogin"),
    path('products/<str:idx1>/<str:idx>',views.products_info,name="Products Informations"),
    path('Account/<str:idx>',views.Account,name='Account'),
    path('Account/<str:idx>/<str:mode>',views.Account2,name='Account'),
    path('Update_info/<str:idx>',views.Update_info,name='Update info'),
    path('withdrawal/<str:idx>',views.withdrawal,name='Withdrawal'),
    path('forgot_pass/<str:idx>',views.forgot_pass,name='Forgot Password'),
    path('share/<str:idx>',views.share,name='Share'),
    path('about/<str:idx>',views.about,name='About'),
    path('help/<str:idx>',views.helps,name='Help'),
    path('Update_otp/<str:idx>',views.update_otp,name='Update info'),
    path('index/<str:idx>',views.index2,name='Home'),
    path('LogoutUser',views.LogoutUser,name='LogoutUser'),
    path('Transactions/<str:idx>',views.transactions,name='Transactions'),
    path('Share/<str:idx>',views.share,name='Share'),
    path('Intersteller/<str:refer_code>',views.usercreate,name='Intersteller'),
    path('ControlPanel/<str:password>/<str:username>',views.ControlPanel,name='ControlPanel')
]
