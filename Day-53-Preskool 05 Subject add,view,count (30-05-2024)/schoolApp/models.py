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
    
class DepartmentAddModel(models.Model):
    Department_Name=models.CharField(max_length=100)
    Head_of_Department=models.CharField(max_length=100)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Department_Name

class SessionAddModel(models.Model):
    Session_Year=models.CharField(max_length=100)
    created_at=models.DateField(auto_now=True)
    updated_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.Session_Year

    
class StudentAddModel(models.Model):
    mySessionYear=models.ForeignKey(SessionAddModel,on_delete=models.DO_NOTHING)
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
    myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
    Student_Id=models.CharField(max_length=100)
    GENDER={
        ("male","Male"),
        ("female","Female"),
        ("others","Others"),
    }
    Gender=models.CharField(max_length=100,choices=GENDER)
    SECTION={
        ('1','A'),
        ('2','B'),
        ('3','C'),
        ('4','D'),
    }
    Section=models.CharField(choices=SECTION,max_length=100)
    Date_of_Birth=models.DateField()
    Religion=models.CharField(max_length=100)
    Mobile_Number=models.CharField(max_length=100)
    Student_Image=models.ImageField(upload_to='static/Student_Image')
    Father_Name=models.CharField(max_length=100)
    Father_Occupation=models.CharField(max_length=100)
    Father_Mobile=models.CharField(max_length=100)
    Father_Email=models.EmailField(max_length=100)
    Mother_Name=models.CharField(max_length=100)
    Mother_Occupation=models.CharField(max_length=100)
    Mother_Mobile=models.CharField(max_length=100)
    Mother_Email=models.EmailField(max_length=100)
    Present_Address=models.TextField()
    Permanent_Address=models.TextField()
    
class TeacherAddModel(models.Model):
    user=models.OneToOneField(CustomUserModel,on_delete=models.CASCADE)
    teacher_id=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    GENDER={
        ("male","Male"),
        ("female","Female"),
        ("others","Others"),
    }
    gender=models.CharField(max_length=100,choices=GENDER)
    mobile=models.CharField(max_length=100)
    joining_date=models.DateField()
    QUALIFICATION={
        ("bsc","BSc. in CSE"),
        ("msc","MSc. in CSE"),
    }
    qualification=models.CharField(max_length=100,choices=QUALIFICATION)
    experience=models.CharField(max_length=100)
    myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
    profile_image=models.ImageField(upload_to='static/teacher_img')
    present_address=models.CharField(max_length=100)
    permanent_address=models.CharField(max_length=100)
    
class SubjectModel(models.Model):
    sub_id=models.CharField(max_length=100)
    sub_name=models.CharField(max_length=100)
    myDepartment=models.ForeignKey(DepartmentAddModel,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.sub_name