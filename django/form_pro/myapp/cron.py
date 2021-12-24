from .models import *

def my_scheduled_job():
  College.objects.create(department='daman',college_name='Chandigrah',course='default',image='istockphoto-1221677097-170667a.jpg')