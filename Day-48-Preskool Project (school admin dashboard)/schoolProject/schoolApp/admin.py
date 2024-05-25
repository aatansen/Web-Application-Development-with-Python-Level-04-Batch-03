from django.contrib import admin
from schoolApp.models import CustomUserModel
# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username']
    
admin.site.register(CustomUserModel,CustomUserModelDisplay)

