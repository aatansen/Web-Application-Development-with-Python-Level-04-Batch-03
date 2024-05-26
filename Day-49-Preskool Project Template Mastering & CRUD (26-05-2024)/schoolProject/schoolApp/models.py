from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):
    USER_TYPE={
        ('1','admin'),
        ('2','teacher'),
        ('3','student'),
    }
    user_type = models.CharField(choices=USER_TYPE,max_length=100)
    user_img = models.ImageField(upload_to='static/user_img')
    def __str__(self):
        return self.username
    
class StudentAddModel(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Username=models.CharField(max_length=100)
    Student_Id=models.CharField(max_length=100)
    GENDER={
        ("male","Male"),
        ("female","Female"),
        ("others","Others"),
    }
    Gender=models.CharField(max_length=100,choices=GENDER)
    Date_of_Birth=models.DateField()
    Class=models.CharField(max_length=100)
    Religion=models.CharField(max_length=100)
    Joining_Date=models.DateField()
    Mobile_Number=models.CharField(max_length=100)
    Admission_Number=models.CharField(max_length=100)
    Section=models.CharField(max_length=100)
    Student_Image=models.ImageField(upload_to='static/Student_Image')
    Father_Name=models.CharField(max_length=100)
    Father_Occupation=models.CharField(max_length=100)
    Father_Mobile=models.CharField(max_length=100)
    Father_Email=models.EmailField(max_length=100)
    Mother_Name=models.CharField(max_length=100)
    Mother_Occupation=models.CharField(max_length=100)
    Mother_Mobile=models.CharField(max_length=100)
    Mother_Email=models.CharField(max_length=100)
    Present_Address=models.CharField(max_length=100)
    Permanent_Address=models.CharField(max_length=100)
    created_by=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.First_Name
    
