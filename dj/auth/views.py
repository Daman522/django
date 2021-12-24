from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import *
from django.http import JsonResponse
# from rest_framework import generics,status
# from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
# from django.contrib.sites.shortcuts import get_current_site

from django.core.mail import EmailMessage

# Create your views here.


# class RegisterView()