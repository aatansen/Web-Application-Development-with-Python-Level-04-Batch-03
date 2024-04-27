from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    picture=models.ImageField(upload_to='static/profilepics')
    dob=models.DateField(auto_now_add=True)
    address=models.TextField()
    BLOOD_GROUP=[
        ('a+','A Positive'),
        ('a-','A Negative'),
        ('b+','B Positive'),
        ('b-','B Negative'),
        ('ab+','AB Positive'),
        ('ab-','AB Negative'),
        ('o+','O Positive'),
        ('o-','O Negative'),
    ]
    blood_group=models.CharField(choices=BLOOD_GROUP,max_length=100)
    USER_TYPE=[
        ('recruiter','Job Recruiter'),
        ('seeker','Job Seeker'),
    ]
    user_type=models.CharField(choices=USER_TYPE,max_length=100)
    
    def __str__(self):
        return self.username