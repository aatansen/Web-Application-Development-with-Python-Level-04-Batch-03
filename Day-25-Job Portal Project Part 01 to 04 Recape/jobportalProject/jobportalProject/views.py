from django.shortcuts import render,redirect
from jobportalApp.models import CustomUserModel
from django.contrib.auth import authenticate,login,logout

def signup(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        picture=request.FILES.get('picture')
        dob=request.POST.get('dob')
        address=request.POST.get('address')
        blood_group=request.POST.get('blood_group')
        user_type=request.POST.get('user_type')
        
        if password==cpassword:
            
            user = CustomUserModel.objects.create_user(
                first_name=fname,
                last_name=lname,
                username=uname,
                email=email,
                password=password,
                picture=picture,
                dob=dob,
                address=address,
                blood_group=blood_group,
                user_type=user_type,
            )
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
        
    return render(request,'signup.html')

def signin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        
        user=authenticate(
            username=uname,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')
    return render(request,'signin.html')

def dashboard(request):
    return render(request,'dashboard.html')



