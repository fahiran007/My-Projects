"""bloggerproject URL Configuration

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
from django.urls import path,include
from iblogger24 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/<str:link_idx>',views.Home),
    path('/Continue/<str:round_idx>/<str:link_idx>',views.roundation),
    path('/Get-Link/<str:round_idx>/<str:link_idx>',views.get_link),
    path('/Download/<str:round_idx>/<str:link_idx>',views.get_link),
]
