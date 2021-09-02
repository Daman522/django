"""mypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myappp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',UpdateProfile,name="profile"),
    path('account/',UpdateAccount,name="account"),
    path('nav/',nav,name="nav"),
    path('reg/',Register,name="register"),
    path('log/',Login,name="login"),
    path('logout',Logout,name="logout"),
    path('click',Click,name="click"),





]








from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    path('',views.home,name="index"),
    path('nav/',views.nav,name="nav"),
    path('login/',views.Log,name="login"),
    path('createaccount/',views.createaccount,name="createaccount"),



    
]
