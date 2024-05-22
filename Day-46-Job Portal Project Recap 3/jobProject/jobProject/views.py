from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from jobApp.models import CustomUserModel,RecruiterProfileModel,SeekerProfileModel,SeekerEducationModel,SeekerWorkExModel,BasicInfoModel,ContactModel

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
            if user.userType=='recruiter':
                RecruiterProfileModel.objects.create(user=user)
            elif user.userType=='seeker':
                SeekerProfileModel.objects.create(user=user)
                SeekerEducationModel.objects.create(user=user)
                SeekerWorkExModel.objects.create(user=user)

            BasicInfoModel.objects.create(user=user)
            ContactModel.objects.create(user=user)
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

def profileinfo(request):
    return render(request,'profileinfo.html')

def recruiterprofile(request):
    return render(request,'recruiter/recruiterprofile.html')

def seekerprofile(request):
    return render(request,'seeker/seekerprofile.html')

def seekereducation(request):
    return render(request,'seeker/seekereducation.html')

def seekerworkex(request):
    return render(request,'seeker/seekerworkex.html')

def basicinfo(request):
    return render(request,'basicinfo.html')

def contactinfo(request):
    return render(request,'contactinfo.html')

def editprofile(request):
    return render(request,'editprofile.html')












