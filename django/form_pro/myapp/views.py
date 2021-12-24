from django import forms
from django.http import request
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from myapp.forms import *
from django.urls import reverse

from django.http import JsonResponse
from myapp.models import *
# Create your views here.
#   def post(self,request):
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             p = Product.objects.create(
#                 name = form.cleaned_data.get('name'),
#                 desc = form.cleaned_data.get('desc'),
#                 price = form.cleaned_data.get('price')
#             )
#             p.save()
#             return HttpResponseRedirect(reverse('success'))
        
#         return render(request,self.temp_name,locals())

def Add(request):
    form =CollegeForm(use_required_attribute=False)
    if request.method=='POST':
        form =CollegeForm(request.POST,use_required_attribute=False)
        print(request.POST)
        print(request.FILES)
       
        if form.is_valid():
            print("Xxxxxxxxxxxxxxxxx")
            print(form.cleaned_data)
            c=College.objects.create(
                department =form.cleaned_data.get('department'),
                college_name=form.cleaned_data.get('college_name'),
                course=form.cleaned_data.get('course'),
                image=request.FILES.get('image')
            )
            c.save()
            # c=College.objects.all()
            return HttpResponse('Submitted')
            # return render(request,'1.html',locals())
        else:
            print("Errr")

    return render(request,'1.html',locals())


def viewall(request):
    if request.method=="POST":
        pass
    c=College.objects.all()
    print(c)
    return render(request,'2.html',locals())

def main_view(request,):
    form=ImageForm(request.POST or None,request.FILES or None)
    print(form)
    if form.is_valid():
        form.save()
        # return HttpResponse('image cropped')
        return HttpResponseRedirect(reverse('view'))
    if request.method=="POST":
        print(request.POST)
        return HttpResponseRedirect(reverse('view'))
    return render(request,'base.html',locals())



