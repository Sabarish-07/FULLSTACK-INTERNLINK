from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    faculty_id=models.CharField(max_length=50,default="null")
    department=models.CharField(max_length=50,default="null")



# Create your models here.
