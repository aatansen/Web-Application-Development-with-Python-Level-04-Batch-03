from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from CaloryCounterApp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        
        if password==cpassword:
            user=CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            user_info=UserInfoModel.objects.create(userinfo=user)
            calory_info=UserInfoModel.objects.create(eaten_by=user)

            user.save()
            user_info.save()
            calory_info.save()

            return redirect('signin')
        
    return render(request,'signup.html')
def signin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')

    user=authenticate(
        username=username,
        password=password,
    )
    if user:
        login(request,user)
        return redirect('dashboard')
    return render(request,'signin.html')

@login_required
def dashboard(request):
    current_user=request.user
    
    user_info=UserInfoModel.objects.get(userinfo=current_user)
    food_item=CaloryItemModel.objects.filter(eaten_by=request.user)

    bmr={
        'user_info':user_info,
        'food_item':food_item,
    }
    
    return render(request,'dashboard.html',bmr)

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addinfo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        
        user_info=UserInfoModel.objects.create(
            userinfo=request.user,
            name=name,
            age=age,
            gender=gender,
            height=height,
            weight=weight,
        )
        user_info.save()
        
        current_user=request.user
        user_info=get_object_or_404(UserInfoModel,userinfo=current_user)
        weight=float(user_info.weight)
        height=float(user_info.height)
        age=float(user_info.age)
        if user_info.gender == 'male':
            result=66.47+(13.75*weight)+(5.003*height)-(6.755*age)
        
        elif user_info.gender == 'female':
            result=65.51+(9.563*weight)+(1.850*height)-(4.676*age)

        user_info.result=result
        user_info.save()

        return redirect('dashboard')
    return render(request,'addinfo.html')

@login_required
def additem(request):
    if request.method=="POST":
        item_name=request.POST.get('item_name')
        calory_consume=request.POST.get('calory_consume')
        
        caloryitem=CaloryItemModel.objects.create(
            item_name=item_name,
            calory_consume=calory_consume,
        )
        caloryitem.save()
        return render(request,'dashboard.html')
    return render(request,'additem.html')










