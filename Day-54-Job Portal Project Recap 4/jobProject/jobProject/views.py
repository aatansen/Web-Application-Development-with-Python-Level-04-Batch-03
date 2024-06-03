from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from jobApp.models import *

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        role=request.POST.get('role')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        profile_picture=request.FILES.get('profile_picture')
        email=request.POST.get('email')
        
        if password==confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                password=password,
                role=role,
                city=city,
                gender=gender,
                profile_picture=profile_picture,
                email=email,
            )
            user.save()
            
            if role=='recruiter':
                role_select=RecruiterModel.objects.create(recruiter_user=user)
              
            else:
                role_select=SeekerModel.objects.create(seeker_user=user)
          
            role_select.save()
            return redirect('signin')
    return render(request,'common/signup.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user_auth = authenticate(
            username=username,
            password=password,
        )
        if user_auth:
            login(request,user_auth)
            return redirect('dashboard')
        
    return render(request,'common/signin.html')

def dashboard(request):
    return render(request,'common/dashboard.html')