from django.db import models

# Create your models here.

class studentModel(models.Model):
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='media/StudentImages')

    def __str__(self):
        return self.Name + self.Department