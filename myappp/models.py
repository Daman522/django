from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.contrib.auth.models import User,AbstractBaseUser




# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f'Name = {self.name }'


class Phone(models.Model):
    price = models.FloatField(max_length=30000,
                        default=0,null="True",blank="True")
    # brand= models.CharField(max_length=300)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name="phone")
    specification=models.IntegerField()

    def __str__(self):
        return f'Price = {self.price} || Brand = {self.brand.name} || ID = {self.brand.id}'


class Profile(models.Model):
    male = "m"
    female = "f"
   
    choices = [
        (male, "Male"),
        (female, "Female"),
        
    ]
    user=models.OneToOneField(User,on_delete=CASCADE,default=4,related_name="profile")
    address=models.CharField(max_length=6000)
    phone=models.IntegerField()
    img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null=True,blank=True)
    money=models.IntegerField(blank=True, null=True)
    account =models.IntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=25, default="", choices=choices)
   
    def __str__(self):
       return f" NAME-- {self.user.username}+ GENDER--{self.gender}" 
   