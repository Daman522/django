from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=('username','email','first_name','last_name')