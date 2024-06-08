from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    def __str__(self):
        return self.username
    
class UserInfoModel(models.Model):
    userinfo=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    GENDER={
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    }
    gender=models.CharField(choices=GENDER,max_length=100)
    height=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    result=models.CharField(max_length=100)
    
    def __str__(self):
        return self.userinfo.username
    
class CaloryItemModel(models.Model):
    eaten_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    item_name=models.CharField(max_length=100)
    calory_consume=models.CharField(max_length=100)
    def __str__(self):
        return self.eaten_by.username
    