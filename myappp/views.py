from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django.shortcuts import redirect, render

from django.urls import reverse
from django.http import HttpResponseRedirect, request, response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import random
from .models import *
import csv
import pandas as pd 
import json
from django.views import View
from django.core.mail import send_mail
import random
from django.conf import settings
# from .helpers import send_forgot_password_email
# import uuid

# Create your views here.

def Click(request):
    arr=[]
    for i in User.objects.all():
        # print(i.last_login)
        d= str(i.last_login)
        c=d[0:10]
        # print(type(c))
        arr.append(c)
    f=open('/home/pulkit/Desktop/Project/mypro/myappp/file.csv','a')
    writer = csv.writer(f)
    writer.writerow(arr)
    data = pd.read_csv('/home/pulkit/Desktop/Project/mypro/myappp/file.csv') 
    df= pd.DataFrame({
        "dates": [data]
    })
    # print("dataframe datan ;;;",df)
    # row1 = df.iloc[1]
    # print(row1)
    f.close()

    b = []
    
    print(type(arr))
    for i in arr:
        print(type(i))
        b.append(i)
        # i.save()

    # arr = [1,2,3]
    return render(request,'navbar.html',locals())

def nav(request):
    u=User.objects.all()
    return render(request,'navbar.html',locals())

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
        
        # if password(len)<=4:
        #      messages.error(request, 'Password is too short')
        if password!=confirm:
            messages.error(request, 'PASSWORD DOESNT MATCH')
            return HttpResponseRedirect(reverse('register'))
        reg.save()

        p = Profile.objects.create(user=reg,address="",phone=91)
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
        request.user.profile.money= request.user.profile.money + int(request.POST.get('money2'))
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
def register(request):
    return render(request, 'register.html')

# def createaccount(request):
#     if request.method=="POST":
#         print(request.POST)
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         confirm=request.POST.get('confirm')
#         address=request.POST.get('address')
#         phone=request.POST.get('phone')
#         gender=request.POST.get('gender')
#         print(email)
#         obj=CreateAccount(name=name,email=email,password=password,address=address,phone=phone,gender=gender)
#         if password!=confirm:
#             return HttpResponse("PASSWORD DOESNT MATCH")

#         else:
#             obj.save()
#             return render(request,'navbar.html') #MESSAGE THAT ACCOUNT IS CREATED 
    
#     else:
        
#         return render(request,'newaccount.html')
    
# def Log(request):
#     if request.method=="POST":
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         obj=CreateAccount.objects.get(email=email)
        
#         return render(request,'login.html')
    
#     else:
#         return render(request,'newaccount.html')

# def post(self,request):
        
#         email=request.POST.get('email')
#         print(email)
#         u = User.objects.filter(email=email).first()
#         if not User.objects.filter(email=email).first():
#             messages.error(request, 'no user found with this email')
#             return HttpResponseRedirect(reverse('forget'))
#             # return HttpResponse('no user found with this email')
#         user_obj=User.objects.get(email=email)
  
#         email= request. POST['email']
#         print(email)
#         if User.objects.filter(email=email).exists() :
#             code = str(random.randint(100000, 999999))
#             path=settings.BASE_URL+"/"+"resetpassword"+"/"+ code
            
#             config = {
#                 'recipients': email,
#                 'email_from': settings.EMAIL_HOST_USER,
#                 'subject': "Reset Password",
#                 'domain': settings.BASE_URL,

#             }

#             send_mail('Link for reset password - Password Reset', config.get('domain') + '/resetpassword' +
#                       '/' + code, 'from@example.com', [email], fail_silently=False)









def NewLogin(request):
    if request.method=="POST":
        print(request.POST)
        res = {
            "error":None,
            "success" : True
        }

        e = request.POST.get('email')
        try:
            user_ = User.objects.get(email=e)
            u = authenticate(request,username=user_.username,password=request.POST.get('password'))
            if u:
                if User.objects.filter(email=e).exists() :
                    code = str(random.randint(100000, 999999))
                    path=settings.BASE_URL+"/"+"verifyaccount"+"/"+ code
                # login(request,u)
                config = {
                'recipients': e,
                'email_from': settings.EMAIL_HOST_USER,
                'subject': "Verify your account",
                'domain': settings.BASE_URL,

            }
                send_mail('Link for verification- Verification', config.get('domain') + '/verifyaccount' +
                '/' + code, 'from@example.com', [e], fail_silently=False)
                forget_entry = ForgetPassword2.objects.create(user=u,code=code)
                forget_entry.save()

            else:
                res['error'] = "Wrong credentials"
                res['success'] = False
        except:
            res['error'] = "No such email exists"
            res['success'] = False

        return HttpResponse(json.dumps(res),content_type='application/json')

    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('nav')
        return render(request,"nlogin.html")



class NewRegister(View):
    def post(self,request):
        res={
            'msg':None,
            'error_username':None,
            'error_email':None,
            'admin': False,
        }
        print(request.POST)
        username=request.POST.get('username')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            res['error_username']='USERNAME ALREADY TAKEN'
            return HttpResponse(json.dumps(res),content_type='application/json')
        if User.objects.filter(email=email).exists():
            res['error_email']='EMAIL ALREADY TAKEN'
            return HttpResponse(json.dumps(res),content_type='application/json')
        else:
            reg=User(username=username,email=email,last_name=last_name)
            reg.set_password(password)
        
        
            if request.POST.get('admin')=="on":
                print(request.user.is_authenticated)
                reg.is_staff=True
                reg.is_superuser=True
                print(reg)
                res['admin']=True
            
            res['msg']='Registered!'
            reg.save()
            
            # send_mail(
            #     'Congratulation! You are Registered ',
            #     'Now you can login!',
            #     'damanpreetkaurameotech@gmail.com',
            #     [email],
            #     fail_silently=False,
            # )
        
        return HttpResponse(json.dumps(res),content_type='application/json')

    def get(self,request):
        return render(request,'nregister.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('nlogin'))


def AddUser(request):
    return render(request,'addnewuser.html')

class ForgetPassword(View):
    template_name="forgot.html"
    def post(self,request):
        
        email=request.POST.get('email')
        print(email)
        u = User.objects.filter(email=email).first()
        if not User.objects.filter(email=email).first():
            messages.error(request, 'no user found with this email')
            return HttpResponseRedirect(reverse('forget'))
            # return HttpResponse('no user found with this email')
        user_obj=User.objects.get(email=email)
    #     token=str(uuid.uuid4())
    #     send_forgot_password_email(user_obj,token)
    #     return HttpResponse('email sent')
        email= request. POST['email']
        print(email)
        if User.objects.filter(email=email).exists() :
            code = str(random.randint(100000, 999999))
            path=settings.BASE_URL+"/"+"resetpassword"+"/"+ code
            
            config = {
                'recipients': email,
                'email_from': settings.EMAIL_HOST_USER,
                'subject': "Reset Password",
                'domain': settings.BASE_URL,

            }

            send_mail('Link for reset password - Password Reset', config.get('domain') + '/resetpassword' +
                      '/' + code, 'from@example.com', [email], fail_silently=False)
          
            forget_entry = ForgetPassword2.objects.create(user=u,code=code)
            forget_entry.save()
           
        else:
            print('email doesnt exits')
            messages.error(request, 'email doesnt exits')
        
        return HttpResponseRedirect(reverse('send'))
        
        
        
        # return render(request,'nlogin.html',locals())
    def get(self,request):
        return render(request,self.template_name,locals())
   

# class ResetPassword(View):
#     template_name="reset.html"
#     def post(self,request,code):
#         email=request.User
#         print(email,'-----------')
#         return HttpResponseRedirect(reverse('nlogin'))
        
        # forget_email= request. POST['forget_email']
        # print(forget_email)
        # if User.objects.filter(email=forget_email).exists() :
            
           
        # else:
        #     print('email doesnt exits')
        # otp= request.POST['otp']
        # new_password= request. POST['new_password']
        # confirm_password= request. POST['confirm_password']

        
        
        # return HttpResponseRedirect(reverse('nlogin'))
        # return render(request,'nlogin.html',locals())
    # def get(self,request):
    #     return render(request,self.template_name,locals())

def VerifyAccount(request,code):
    if request.method == "GET":
        print(code)
        e = request.POST.get('email')
        print(e,'emaiiilllll')
        try:
            obj=ForgetPassword2.objects.get(code=code)
            print(obj,'---------')
            user_ = User.objects.get(email=e)
            u = authenticate(request,username=user_.username,password=request.POST.get('password'))
            print(u,'uuuuuuuuu')
            login(request,u)
            print(obj.user)
        except Exception as e:
            print(e,'eeeeeeee')
            # login(request,u)

        return render(request,'nlogin.html',locals()) 







def ResetPassword(request,code):
    
    if request.method == "GET":
        print(code)
        try:
            obj=ForgetPassword2.objects.filter(code=code).first()
            print(obj.user)
        except Exception as e:
            print(e)

        return render(request,'reset.html',locals()) 


    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST.get('user'))
            new_password=request.POST.get('new_password')
            confirm_password=request.POST.get('confirm_password')
            if new_password==confirm_password:
                user.set_password(request.POST.get('new_password'))
                user.save()
                messages.success(request, 'Password changed')
                return redirect(reverse('nlogin'))
            else:
                messages.error(request, 'Password doesnt match')
                return redirect(reverse('resetpassword'))
        except Exception as e:
            print(e)
            return redirect(reverse('forget'))


def EmailSend(request):
    return render(request,'emailsend.html') 
   
def EditButton(request,id):
    if request.method=="POST":
        detail = User.objects.get(id=request.POST.get('userid'))
        if detail:
            detail.email = request.POST.get('email')
            detail.last_name = request.POST.get('last_name')
            detail.save()
            messages.success(request, 'updatedd')
            return redirect(reverse('edit',kwargs={'id':detail.id}))
            
    else:
        detail = User.objects.get(id=id)
        return render(request,'edit.html',locals())

    # if request.method=="POST":
    #     print(request.POST,'------')
    #     request.user.email = request.POST.get('email')
    #     request.user.last_name = request.POST.get('last_name')
    #     request.user.save()
    #     return HttpResponseRedirect(reverse('edit')) 

    return render(request,'edit.html')

def DeleteButton(request,id):
    
    detail = User.objects.filter(id=id)
    print(detail,'------')
    messages.error(request, 'deleted')
    detail.delete()
    
    return HttpResponseRedirect(reverse('nav'))