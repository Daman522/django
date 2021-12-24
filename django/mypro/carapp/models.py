from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_code = models.CharField(max_length=280)

    def __str__(self):
        return f"Name - {self.location_name} || Code - {self.location_code}"


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    company_ceo = models.CharField(max_length=280)
    company_startup = models.CharField(max_length=100)
    company_location = models.ForeignKey(
        Location, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f" NAME - {self.company_name} || CEO- {self.company_ceo}||DATE- {self.company_startup}"


class Car(models.Model):
    car_name = models.CharField(max_length=300)
    car_price = models.IntegerField()
    car_color = models.CharField(max_length=200)
    car_topspeed = models.FloatField(default=0)
    car_modelyear = models.IntegerField()
    car_milage = models.FloatField()
    car_company = models.ForeignKey(
        Company, on_delete=models.CASCADE, default=1, related_name="car")

    def __str__(self):
        return f"NAME - {self.car_name} || COLOR - {self.car_color} || PRICE - {str(self.car_price)}"


class Place(models.Model):
    place_name = models.CharField(max_length=50,null=True)
    place_address = models.CharField(max_length=80,null=True)

    def __str__(self):
        return "Place name is :{0} and Address is : {1} ".format(self.place_name, self.place_address)


class Restrurant(models.Model):
    place = models.OneToOneField(Place, on_delete=CASCADE)
    rest_name = models.CharField(max_length=200)
    rest_dish = models.CharField(max_length=600)

    def __str__(self):
        return "Resturant name--{0} || Place {1} ".format(self.rest_name, self.place)
