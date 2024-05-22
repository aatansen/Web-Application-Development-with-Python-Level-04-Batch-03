from django.contrib import admin
from jobApp.models import CustomUserModel
# Register your models here.

class CustomUserModelDisplay(admin.ModelAdmin):
    list_display=['username','userType']
admin.site.register(CustomUserModel,CustomUserModelDisplay)
