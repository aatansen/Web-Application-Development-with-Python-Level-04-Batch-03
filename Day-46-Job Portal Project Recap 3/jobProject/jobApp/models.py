from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    profilePhoto = models.ImageField(upload_to='static/user_profile')
    age=models.CharField(max_length=100)
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    gender=models.CharField(choices=GENDER,max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    bloodGroup=models.CharField(max_length=100)
    USER_TYPE=[
        ('seeker','Job Seeker'),
        ('recruiter','Job Recruiter'),
    ]
    userType = models.CharField(choices=USER_TYPE,max_length=100)
    
    def __str__(self):
        return self.username