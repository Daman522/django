from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from django.urls import reverse
from django.http import HttpResponseRedirect, request
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import random



# Create your views here.
def nav(request):
    return render(request,'navbar.html')

def Register(request):
    if request.method=="POST":
        print(request.POST)
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm=request.POST.get('confirm')
        reg=User(username=username,email=email)
        reg.set_password(password)
        if User.objects.filter(username=username).exists():
            messages.error(request, 'USERNAME ALREADY TAKEN')
            return HttpResponseRedirect(reverse('register'))
            #  return HttpResponse("USERNAME ALREADY TAKEN")
        
       
        if password!=confirm:
            messages.error(request, 'PASSWORD DOESNT MATCH')
            return HttpResponseRedirect(reverse('register'))
        reg.save()

        p = Profile.objects.create(user=reg,address="punjab",phone=1234)
        account = random.randint(190000,250000)
        p.account = account
        p.save()

        messages.success(request, 'Now you can login!')
        return HttpResponseRedirect(reverse('login'))

    return render(request,'register.html')

def Login(request):
    if request.method=="POST":
        print(request.POST)
        email= request.POST['email']
        password = request.POST['password']
        user_= User.objects.filter(email=email).first()
        user = authenticate(request,username=user_.username, password=password)
        if user is not None:
            login(request, user)
        messages.success(request, 'LOGGED IN!!')
        return HttpResponseRedirect(reverse('nav'))
    else:
       return render(request,'login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def createaccount(request):
    if request.method=="POST":
        print(request.POST)
    #     # name=request.POST.get('name')
    #     # email=request.POST.get('email')
    #     # password=request.POST.get('password')
    #     # confirm=request.POST.get('confirm')
    #     address=request.POST.get('address')
    #     phone=request.POST.get('phone')
    #     gender=request.POST.get('gender')
    #     print(email)
    #     obj=CreateAccount(name=name,email=email,password=password,address=address,phone=phone,gender=gender)
    #     if password!=confirm:
    #         return HttpResponse("PASSWORD DOESNT MATCH")

    #     else:
    #         obj.save()
    #         return render(request,'navbar.html') #MESSAGE THAT ACCOUNT IS CREATED 
    
    # else:
        
    #     return render(request,'newaccount.html')

def UpdateProfile(request):
    if request.method=="POST":
        print(request.POST)
        request.user.profile.phone=request.POST.get('phone')
        request.user.profile.address=request.POST.get('address')
        request.user.profile.gender=request.POST.get('gender')
        # request.user.profile.money=request.POST.get('money')
        request.user.profile.save()
        return HttpResponseRedirect(reverse('profile'))
    return render(request,'newaccount.html')

def UpdateAccount(request):
    if request.method=="POST":

        request.user.first_name = request.POST.get('firstname')
        request.user.last_name = request.POST.get('lastname')
        request.user.username = request.POST.get('username')
        request.user.email = request.POST.get('email')
        if request.POST.get('admin')=="on":
            request.user.is_staff=True
            request.user.is_superuser=True
        else:
            request.user.is_staff=False
            request.user.is_superuser=False
        request.user.save()
        return HttpResponseRedirect(reverse('account'))
    return render(request,'account.html')