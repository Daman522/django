from django.db import models

# Create your models here.
class College(models.Model):
    department=models.CharField(max_length=200)
    college_name=models.CharField(max_length=100)
    course=models.CharField(max_length=60,default='')
    image=models.ImageField(upload_to='images',blank=True,null=True)

    def __str__(self):
        return self.college_name


class Image(models.Model):
    file=models.ImageField(upload_to='images',blank=True,null=True)
    uploaded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)