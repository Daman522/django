from django.shortcuts import render

from django.http import HttpResponseRedirect

# Create your views here.
def register(request):
    return render(request, 'register.html')

def createaccount(request):
    if request.method=="POST":
        print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm=request.POST.get('confirm')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        print(email)
        obj=CreateAccount(name=name,email=email,password=password,address=address,phone=phone,gender=gender)
        if password!=confirm:
            return HttpResponse("PASSWORD DOESNT MATCH")

        else:
            obj.save()
            return render(request,'navbar.html') #MESSAGE THAT ACCOUNT IS CREATED 
    
    else:
        
        return render(request,'newaccount.html')
    
def Log(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=CreateAccount.objects.get(email=email)
        
        return render(request,'login.html')
    
    else:
        return render(request,'newaccount.html')
