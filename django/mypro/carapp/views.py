from django.http.response import HttpResponse
from django.shortcuts import redirect, render, resolve_url
import csv
from .models import *
from django.http import JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.views import View
from django.http import JsonResponse
import json
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if request.POST.get('email')== "":
            messages.error(request,'email required')
            return redirect('index')
        
        elif request.POST.get('password')== "":
            messages.error(request,'password required')
            return redirect('index')
        if User.objects.filter(username=username).exists():
          messages.error(request,'username exists')
          return redirect('index')
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already taken')
            return redirect('index')
        else:
            u=User.objects.create(username=username,email=email)
            u.set_password(password)
            u.save()
            
            messages.error(request,'REGISTERED')
            return redirect('login')
    return render(request,'register.html')

class NewLogin(View):
    def get(self,request):
        return render(request,'login.html')


    def post(self,request):
        print(request.POST,'REQ-----')
        data = {}  
        email = request.POST.get('email')
        password= request.POST.get('password')
        print(email,'eeee')
        print(password,'---pppp')
        try:
            user_ = User.objects.get(email=email)
            print(user_,'user-------')
            user = authenticate(request,username=user_.username, password=password)
            print(user,'userrr-0')
            if user is not None:
                login(request, user)
                messages.success(request,'User login Successfull')
                data['status'] = True
                data['message'] = 'User login Successfull'
                # return redirect('index')
            else:
                data['status'] = False
                messages.error(request,'Invalid Credential')
                # return redirect('login')
                data['message'] = 'Invalid Credential'
            return HttpResponse(json.dumps(data), content_type='application/json')
        except Exception as e:
            messages.error(request,'Email doesnt exists')
            data['message'] = 'Email doesnt exists'
            return HttpResponse(json.dumps(data), content_type='application/json')
    # return render(request,'login.html')






# def newlogin(request):
#     data = {}   
#     if request.method=="POST":
       
#         email=request.POST.get('email')
#         password=request.POST.get('password')
       
#         user_= User.objects.filter(email=email).first()
#         user = authenticate(request,username=user_.username, password=password)
#         print(user,'userrr-0')
#         if user is not None:
#             login(request, user)
#             messages.success(request,'User login Successfull')
#             data['status'] = True
#             data['message'] = 'User login Successfull'
#             # return redirect('index')
#         else:
#             data['status'] = False
#             messages.error(request,'Invalid Credential')
#             # return redirect('login')
#             data['message'] = 'Invalid Credential'
#         return HttpResponse(json.dumps(data), content_type='application/json')
#     return render(request,'login.html')
    # 



# class Firstmiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request ):
#         response= self.get_response(request)
#         return render(request,"index.html",{'d':response})

def show(request):
    car=Car.objects.all()
    return JsonResponse({car:list(car.values())})


def add(request):
    if request.method=="POST":
        print(request.POST,'---RRRR')
        place_name=request.POST.get('place_name')
        place_address=request.POST.get('place_address')

        p=Place.objects.create(place_name=place_name,place_address=place_address)
        print(p,'ppppp')
        p.save()
        return HttpResponse('ADDEDDD')
    return render(request,'addplace.html')




def show(request):
    if request.method=="POST":
        pass
    p=Place.objects.all()
    return render(request,'show.html',locals())


def edit(request):
    return render(request,'index.html')

def delete(request):
    # return render(request,'index.html')
    p=Place.objects.filter(id=id)
    
    messages.error(request, 'deleted')
    p.delete()