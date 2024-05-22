from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from jobApp.models import CustomUserModel

def signup(request):
    if request.method == "POST":
        profilePhoto = request.FILES.get('profilePhoto')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        bloodGroup = request.POST.get('bloodGroup')
        userType = request.POST.get('userType')
        
        if password==confirmPassword:
            user = CustomUserModel.objects.create_user(
                profilePhoto=profilePhoto,
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                age=age,
                gender=gender,
                city=city,
                country=country,
                bloodGroup=bloodGroup,
                userType=userType,
            )
            user.save()
            return redirect('signin')
    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login(request,user)
            return redirect('dashboard')
    return render(request,'signin.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')

def logoutpage(request):
    logout(request)
    return redirect('signin')

def profile(request):
    return render(request,'profile.html')