from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
