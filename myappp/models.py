from django.db import models
from django.db.models.fields import related

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


class Register(models.Model):
    male = "m"
    female = "f"
   
    choices = [
        (male, "Male"),
        (female, "Female"),
        
    ]
    name=models.CharField(max_length=500)
    email=models.EmailField(null=False)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=6000)
    phone=models.IntegerField()
    img=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    gender = models.CharField(
        max_length=25, default="", choices=choices)
   